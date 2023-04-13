from django import forms

from .models import Hotel


class CreateHotelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['type'].empty_label = 'Type not selected'

    class Meta:
        model = Hotel
        fields = ['name', 'type', 'activities', 'loss', 'price_single_type_room',
                  'price_double_type_room', 'price_president_type_room']


class UpdateHotelForm(forms.ModelForm):
    class Meta:
        model = Hotel
        fields = ['name', 'price_single_type_room', 'price_double_type_room', 'price_president_type_room']
