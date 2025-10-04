from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.http import JsonResponse
from .models import Order, OrderItem
from .forms import OrderForm, OrderItemForm
from menu.models import Item

class OrderListView(ListView):
    model = Order
    template_name = 'order_list.html'
    context_object_name = 'orders'
    ordering = ['-created_at']

@method_decorator(login_required, name='dispatch')
class OrderCreateView(CreateView):
    model = Order
    form_class = OrderForm
    template_name = 'order_create.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        # After creating an order, redirect to add items
        return redirect('orders:add_items', pk=self.object.pk)

@method_decorator(login_required, name='dispatch')
class OrderDetailView(DetailView):
    model = Order
    template_name = 'order_detail.html'
    context_object_name = 'order'

@method_decorator(login_required, name='dispatch')
class OrderUpdateView(UpdateView):
    model = Order
    form_class = OrderForm
    template_name = 'order_create.html'

    def get_success_url(self):
        return reverse_lazy('orders:order_detail', kwargs={'pk': self.object.pk})

@method_decorator(login_required, name='dispatch')
class OrderDeleteView(DeleteView):
    model = Order
    template_name = 'order_confirm_delete.html'
    success_url = reverse_lazy('orders:order_list')

@login_required
def add_items_to_order(request, pk):
    order = get_object_or_404(Order, pk=pk)
    if request.method == 'POST':
        form = OrderItemForm(request.POST)
        if form.is_valid():
            order_item = form.save(commit=False)
            order_item.order = order
            order_item.save()
            return redirect('orders:add_items', pk=order.pk)
    else:
        form = OrderItemForm()

    items = order.items.select_related('item').all()
    total = order.total_price()
    context = {'order': order, 'form': form, 'items': items, 'total': total}
    return render(request, 'order_add_items.html', context)

@login_required
def remove_order_item(request, order_pk, item_pk):
    order = get_object_or_404(Order, pk=order_pk)
    item = get_object_or_404(OrderItem, pk=item_pk, order=order)
    item.delete()
    return redirect('orders:add_items', pk=order.pk)

# Customer cart functionality
def get_or_create_cart(request):
    """Get or create a cart for the current user/session"""
    if request.user.is_authenticated:
        cart, created = Order.objects.get_or_create(
            user=request.user,
            status='cart',
            defaults={'customer_name': request.user.username}
        )
    else:
        # For anonymous users, we'll use session-based cart
        session_key = request.session.session_key
        if not session_key:
            request.session.create()
            session_key = request.session.session_key
        
        cart, created = Order.objects.get_or_create(
            customer_name=f"Guest_{session_key[:8]}",
            status='cart',
            defaults={'phone': 'N/A'}
        )
    return cart

def add_to_cart(request, item_id):
    """Add item to cart"""
    item = get_object_or_404(Item, pk=item_id)
    cart = get_or_create_cart(request)
    
    # Check if item already in cart
    order_item, created = OrderItem.objects.get_or_create(
        order=cart,
        item=item,
        defaults={'quantity': 1}
    )
    
    if not created:
        order_item.quantity += 1
        order_item.save()
    
    messages.success(request, f'{item.name} added to cart!')
    return redirect('menu:customer_menu')

def cart_view(request):
    """View cart contents"""
    cart = get_or_create_cart(request)
    items = cart.items.select_related('item').all()
    total = cart.total_price()
    
    context = {
        'cart': cart,
        'items': items,
        'total': total,
    }
    return render(request, 'orders/cart.html', context)

def update_cart_item(request, item_id):
    """Update quantity of item in cart"""
    cart = get_or_create_cart(request)
    order_item = get_object_or_404(OrderItem, order=cart, item_id=item_id)
    
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))
        if quantity <= 0:
            order_item.delete()
        else:
            order_item.quantity = quantity
            order_item.save()
    
    return redirect('orders:cart')

def remove_from_cart(request, item_id):
    """Remove item from cart"""
    cart = get_or_create_cart(request)
    order_item = get_object_or_404(OrderItem, order=cart, item_id=item_id)
    order_item.delete()
    messages.info(request, f'{order_item.item.name} removed from cart')
    return redirect('orders:cart')

def checkout(request):
    """Checkout process"""
    cart = get_or_create_cart(request)
    
    if request.method == 'POST':
        # Update cart with customer info
        cart.customer_name = request.POST.get('customer_name', '')
        cart.phone = request.POST.get('phone', '')
        cart.payment_method = request.POST.get('payment_method', 'cash')
        cart.status = 'pending'
        cart.save()
        
        messages.success(request, 'Order placed successfully! We will contact you soon.')
        return redirect('orders:order_success', order_id=cart.id)
    
    context = {
        'cart': cart,
        'items': cart.items.select_related('item').all(),
        'total': cart.total_price(),
    }
    return render(request, 'orders/checkout.html', context)

def order_success(request, order_id):
    """Order success page"""
    order = get_object_or_404(Order, pk=order_id)
    context = {'order': order}
    return render(request, 'orders/order_success.html', context)

@login_required
def my_orders(request):
    """Display a user's order history"""
    orders = Order.objects.filter(
        user=request.user,
        status__in=['pending', 'processing', 'completed', 'cancelled']
    ).order_by('-created_at')
    
    context = {
        'orders': orders,
        'title': 'My Orders'
    }
    return render(request, 'orders/my_orders.html', context)
