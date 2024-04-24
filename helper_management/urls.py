from django.urls import path
from .views import index, AddCustomer,AddHelper,AssignHelperView
from .views import CustomerListView,CustomerDetailView,HelperDetailView
from .views import remove_helper,remove_customer,HelperListView,free_helper_list

urlpatterns = [
    path('', index, name='home'),
    # Add other app-specific URLs here
    path('addCustomer/',  AddCustomer.as_view(), name='addCustomer'),
    path('addHelper/',  AddHelper.as_view(), name='AddHelper'),
     path('assign/', AssignHelperView.as_view(), name='assign_helper'),
     path('list/', CustomerListView.as_view(), name='customer_list'),
     path('customer_details/<int:pk>/', CustomerDetailView.as_view(), name='customer_details'),
     path('helper_details/<int:pk>/', HelperDetailView.as_view(), name='helper_details'),
     path('remove_helper/<int:customer_id>/', remove_helper, name='remove_helper'),
     path('remove_customer/<int:helper_id>/', remove_customer, name='remove_customer'),
     path('helpers/', HelperListView.as_view(), name='helper_list'),
     path('free_helpers/', free_helper_list, name='free_helper_list'),


     
]