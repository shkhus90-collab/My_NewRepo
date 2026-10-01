from django import forms
from .models import MenuItem, Order

class MenuItemForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = ['name', 'category', 'description', 'price', 'image', 'is_available']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'is_available': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['customer_name', 'customer_phone']
        widgets = {
            'customer_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}),
            'customer_phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'}),
        }