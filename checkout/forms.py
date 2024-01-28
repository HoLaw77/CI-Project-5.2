from django import forms
from .models import Order

class ConfirmOrder(forms.ModelForm):
    class Meta:
        model = Order
        fields = ("full_name", "country", 
    "email", "phone_number", "address1", "address2", "postcode")

def __init__(self, *args, **kwargs):
    """Add placeholder for form fields"""

    super().__init__(*args, **kwargs)
    placeholders = {

        "full_name": "Full Name",  
        "email": "Your Email", 
        "phone_number": "Phone Number", 
        "address1": "Address Line 1", 
        "address2": "Address Line 2", 
        "postcode": "Postcode", 
        "country": "Country",
    }
    
    self.fields['full_name'].required = True
    self.fields['email'].required = True
    self.fields['address1'].required = True
    self.fields['country'].required = True

    for field in self.fields:
        if self.fields[field].required:
            placeholder = f'{placeholder[field]} *'

    