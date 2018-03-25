from django.forms import ModelForm

from .models import Kruk, KrukComment


class AddKrukForm(ModelForm):
    class Meta:
        model = Kruk
        fields = ['content']

class AddKrukCommentForm(ModelForm):
    class Meta:
        model = KrukComment
        fields = ['content']
