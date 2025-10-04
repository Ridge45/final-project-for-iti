from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils.decorators import method_decorator
from .models import Customer

def staff_required(view_func):
    return user_passes_test(lambda u: u.is_active and (u.is_staff or u.is_superuser))(view_func)


@method_decorator([login_required, staff_required], name='dispatch')
class CustomerListView(ListView):
    model = Customer
    template_name = 'customer_list.html'
    context_object_name = 'customers'

def staff_required(view_func):
    return user_passes_test(lambda u: u.is_active and (u.is_staff or u.is_superuser))(view_func)


@method_decorator([login_required, staff_required], name='dispatch')
class CustomerCreateView(CreateView):
    model = Customer
    fields = ['name','email','phone','address']
    template_name = 'customer_form.html'
    success_url = reverse_lazy('customers:customer_list')

@method_decorator([login_required, staff_required], name='dispatch')
class CustomerUpdateView(UpdateView):
    model = Customer
    fields = ['name','email','phone','address']
    template_name = 'customer_form.html'
    success_url = reverse_lazy('customers:customer_list')

@method_decorator([login_required, staff_required], name='dispatch')
class CustomerDeleteView(DeleteView):
    model = Customer
    template_name = 'customer_confirm_delete.html'
    success_url = reverse_lazy('customers:customer_list')

class CustomerDetailView(DetailView):
    model = Customer
    template_name = 'customer_detail.html'
    context_object_name = 'customer'
