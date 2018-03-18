from django.forms import ModelForm

from .models import Kruk


class AddKrukForm(ModelForm):
    class Meta:
        model = Kruk
        fields = ['content']
