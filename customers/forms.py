from django import forms

from .models import Customer


class CustomerCreateForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'middle_name', 'gender',
                  'passport_number', 'disability', ]
