from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils.decorators import method_decorator
from django.shortcuts import render
from .models import Item

class ItemListView(ListView):
    model = Item
    template_name = 'item_list.html'
    context_object_name = 'items'
    paginate_by = 20
    ordering = ['name']  # Fix pagination warning

    def get_queryset(self):
        qs = super().get_queryset()
        q = self.request.GET.get('q')
        if q:
            qs = qs.filter(name__icontains=q)
        return qs

class CustomerMenuView(ListView):
    model = Item
    template_name = 'customer_menu.html'
    context_object_name = 'items'
    paginate_by = 20
    ordering = ['name']

    def get_queryset(self):
        qs = super().get_queryset()
        q = self.request.GET.get('q')
        if q:
            qs = qs.filter(name__icontains=q)
        return qs

def staff_required(view_func):
    return user_passes_test(lambda u: u.is_active and (u.is_staff or u.is_superuser))(view_func)


@method_decorator([login_required, staff_required], name='dispatch')
class ItemCreateView(CreateView):
    model = Item
    fields = ['name', 'price', 'description', 'image']
    template_name = 'item_form.html'
    success_url = reverse_lazy('menu:item_list')

@method_decorator([login_required, staff_required], name='dispatch')
class ItemUpdateView(UpdateView):
    model = Item
    fields = ['name', 'price', 'description', 'image']
    template_name = 'item_form.html'
    success_url = reverse_lazy('menu:item_list')

@method_decorator([login_required, staff_required], name='dispatch')
class ItemDeleteView(DeleteView):
    model = Item
    template_name = 'item_confirm_delete.html'
    success_url = reverse_lazy('menu:item_list')