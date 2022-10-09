from django import forms

from .models import Manufacturer

class ManufacturersForm(forms.Form):

    select_choises = [("0", "Все")]
    for manufacturer in Manufacturer.objects.all():
        select_choises.append((manufacturer.id, manufacturer.name_model))

    car_model = forms.ChoiceField(choices=tuple(select_choises), label='Модель:')

