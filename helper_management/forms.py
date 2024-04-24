from django import forms
from .models import Customer, Helper

class AssignHelperForm(forms.Form):
    customer = forms.ModelChoiceField(queryset=Customer.objects.all())
    helper = forms.ModelChoiceField(queryset=Helper.objects.all())

    def clean(self):
        cleaned_data = super().clean()
        customer = cleaned_data.get('customer')
        helper = cleaned_data.get('helper')
        
        
        # Check if the customer already has a helper assigned
        if customer and customer.assigned_helper:
            raise forms.ValidationError("This customer already has a helper assigned.")
        if helper and Customer.objects.filter(assigned_helper=helper).exists():
            raise forms.ValidationError("This helper is already assigned to a customer.")
        
        return cleaned_data
