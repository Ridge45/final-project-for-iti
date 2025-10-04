from django.urls import path
from .views import ItemListView, ItemCreateView, ItemUpdateView, ItemDeleteView, CustomerMenuView

app_name = 'menu'

urlpatterns = [
    path('', ItemListView.as_view(), name='item_list'),
    path('customer/', CustomerMenuView.as_view(), name='customer_menu'),
    path('add/', ItemCreateView.as_view(), name='item_add'),
    path('<int:pk>/edit/', ItemUpdateView.as_view(), name='item_edit'),
    path('<int:pk>/delete/', ItemDeleteView.as_view(), name='item_delete'),
]
