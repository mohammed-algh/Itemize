from django import forms
from .models import Item

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = [
            'name',
            'description',
            'category',
            'quantity',
            'purchase_date',
            'price',
            'serial_number',
            'warranty_expiry',
            'location',
            'notes',
            'image'
        ]

        widgets = {
            'purchase_date': forms.DateInput(attrs={'type': 'date'}),
            'warranty_expiry': forms.DateInput(attrs={'type': 'date'}),
        }