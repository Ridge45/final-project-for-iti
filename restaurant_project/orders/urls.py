from django.urls import path
from .views import (OrderCreateView, OrderDetailView, OrderUpdateView, OrderDeleteView,
                    add_items_to_order, remove_order_item, OrderListView,
                    add_to_cart, cart_view, update_cart_item, remove_from_cart,
                    checkout, order_success, my_orders)

app_name = 'orders'
urlpatterns = [
    # Admin order management
    path('', OrderListView.as_view(), name='order_list'),
    path('add/', OrderCreateView.as_view(), name='order_add'),
    path('<int:pk>/detail/', OrderDetailView.as_view(), name='order_detail'),
    path('<int:pk>/edit/', OrderUpdateView.as_view(), name='order_edit'),
    path('<int:pk>/delete/', OrderDeleteView.as_view(), name='order_delete'),

    # add items step
    path('<int:pk>/items/', add_items_to_order, name='add_items'),
    path('<int:order_pk>/items/<int:item_pk>/remove/', remove_order_item, name='remove_item'),
    
    # Customer cart functionality
    path('cart/', cart_view, name='cart'),
    path('add-to-cart/<int:item_id>/', add_to_cart, name='add_to_cart'),
    path('update-cart/<int:item_id>/', update_cart_item, name='update_cart_item'),
    path('remove-from-cart/<int:item_id>/', remove_from_cart, name='remove_from_cart'),
    path('checkout/', checkout, name='checkout'),
    path('order-success/<int:order_id>/', order_success, name='order_success'),
    path('my-orders/', my_orders, name='my_orders'),
]
