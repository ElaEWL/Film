from django import forms

from .models import Ocena

class PostForm(forms.ModelForm):

    class Meta:
        model = Ocena
        fields = ('wartość', 'film',)