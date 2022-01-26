from django import forms
from .models import *

class AddVehicleForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['brand'].empty_label = "Марка не выбрана"

    class Meta:
        model = Vehicle
        fields = "__all__"

