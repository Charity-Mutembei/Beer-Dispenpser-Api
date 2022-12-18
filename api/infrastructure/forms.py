from django.forms import ModelForm
from .models import Dispense

class DispenseForm(ModelForm):
    class Meta:
        model = Dispense
        fields = '__all__'