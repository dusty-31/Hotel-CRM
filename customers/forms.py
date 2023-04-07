from django import forms

from .models import Customer


class CustomerCreateForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'middle_name', 'gender',
                  'passport_number', 'disability', ]


class CustomerUpdateForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={"readonly": True}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={"readonly": True}))
    middle_name = forms.CharField(widget=forms.TextInput(attrs={"readonly": True}))
    # gender = forms.ChoiceField()
    passport_number = forms.CharField(widget=forms.TextInput())
    disability = forms.CharField(widget=forms.TextInput())

    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'middle_name', 'gender',
                  'passport_number', 'disability', ]
