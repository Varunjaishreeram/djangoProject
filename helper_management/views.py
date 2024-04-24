from django.shortcuts import render, reverse
from django.contrib import messages
from django.views.generic.edit import CreateView
from .models import Customer,Helper
from django.views.generic import FormView
from .forms import AssignHelperForm
from django.views.generic import ListView, DeleteView,DetailView
from django.shortcuts import redirect, get_object_or_404
from django.views.decorators.http import require_POST

def index(request):
    return render(request, 'index.html')

class CustomerListView(ListView):
    model = Customer
    template_name = 'customer_list.html'
    context_object_name = 'customers'

@require_POST
def remove_customer(request, helper_id):
    helper = get_object_or_404(Helper, pk=helper_id)
    customer = get_object_or_404(Customer, pk=helper.customer.pk)
    if helper.customer:
        
        # Remove the assigned customer from the helper
        helper.customer = None
        customer.assigned_helper = None
        customer.save()
        helper.save()
    # Redirect back to the helper detail page
    return redirect('helper_details', pk=helper_id)

@require_POST
def remove_helper(request, customer_id):
    customer = get_object_or_404(Customer, pk=customer_id)
    if customer.assigned_helper:
        # Remove the assigned helper from the customer
        customer.assigned_helper = None
        customer.save()
    # Redirect back to the customer detail page
    return redirect('customer_details', pk=customer_id)

class HelperListView(ListView):
    model = Helper
    template_name = 'helper_list.html'  
    context_object_name = 'helpers' 

def free_helper_list(request):
    free_helpers = Helper.objects.filter(customer__isnull=True)
    return render(request, 'free_helper_list.html', {'free_helpers': free_helpers})


class CustomerDetailView(DetailView):
    model = Customer
    template_name = 'customer_detail.html'  
    context_object_name = 'customer' 

class HelperDetailView(DetailView):
    model = Helper
    template_name = 'helper_detail.html' 
    context_object_name = 'helper'

class AddCustomer(CreateView):
    model = Customer
    fields = ['name', 'address', 'phone_number', 'email']
    template_name = 'addCustomer.html'
    
    def get_success_url(self):
        return reverse('home')
    
    def form_valid(self, form):
        messages.success(self.request, 'Customer added successfully!')
        return super().form_valid(form)
 
 

class AddHelper(CreateView):
    model = Helper
    fields = ['name', 'gender', 'skill', 'age']
    template_name = 'addHelper.html'
    
    def get_success_url(self):
        return reverse('home')
    
    def form_valid(self, form):
        messages.success(self.request, 'helper added successfully!')
        return super().form_valid(form)

class AssignHelperView(FormView):
    template_name = 'assign_helper.html'
    form_class = AssignHelperForm
    success_url = '/'

    def form_valid(self, form):
        customer = form.cleaned_data['customer']
        helper = form.cleaned_data['helper']
        customer.assigned_helper = helper
        customer.save()
        return super().form_valid(form)

