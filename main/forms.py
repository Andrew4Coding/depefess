from django.forms import ModelForm
from main.models import Menfess

class MenfessEntryForm(ModelForm):
    class Meta:
        model = Menfess
        fields = ['from_who', 'to_who', 'message']