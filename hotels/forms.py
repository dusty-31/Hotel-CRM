from django import forms

from .models import Hotel, HotelType, Activity


class CreateHotelForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter name hotel',
    }))
    type = forms.ModelChoiceField(queryset=HotelType.objects.all(),
                                  widget=forms.Select(attrs={
                                      'class': 'form-control',
                                  }))
    price_single_type_room = forms.IntegerField(widget=forms.NumberInput(attrs={
        'class': 'form-control',
    }))
    price_double_type_room = forms.IntegerField(widget=forms.NumberInput(attrs={
        'class': 'form-control',
    }))
    price_president_type_room = forms.IntegerField(widget=forms.NumberInput(attrs={
        'class': 'form-control',
    }))
    activities = forms.ModelMultipleChoiceField(
        queryset=Activity.objects.all(),
        widget=forms.CheckboxSelectMultiple(),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['type'].empty_label = 'Type not selected'

    class Meta:
        model = Hotel
        fields = ['name', 'type', 'price_single_type_room', 'price_double_type_room', 'price_president_type_room',
                  'activities']


class UpdateHotelForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
    }))
    price_single_type_room = forms.IntegerField(widget=forms.NumberInput(attrs={
        'class': 'form-control',
    }))
    price_double_type_room = forms.IntegerField(widget=forms.NumberInput(attrs={
        'class': 'form-control',
    }))
    price_president_type_room = forms.IntegerField(widget=forms.NumberInput(attrs={
        'class': 'form-control',
    }))

    class Meta:
        model = Hotel
        fields = ['name', 'price_single_type_room', 'price_double_type_room', 'price_president_type_room']
