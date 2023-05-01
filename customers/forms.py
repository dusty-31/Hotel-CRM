from django import forms

from .models import Customer

DISABILITY_CHOICES = [
    (True, 'Yes'), (False, 'No')
]


class CustomerForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter First Name',
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter Last Name',
    }))
    middle_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter Middle Name',
    }))
    passport_number = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': "Passport Number",
    }))
    gender = forms.ChoiceField(choices=Customer.GENDER_CHOICES, widget=forms.RadioSelect())
    disability = forms.ChoiceField(choices=DISABILITY_CHOICES, widget=forms.RadioSelect())

    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'middle_name', 'gender',
                  'passport_number', 'disability', ]
