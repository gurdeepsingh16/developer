from django import forms
from .models import *


class tut_form(forms.ModelForm):
    class Meta:
        model = tut
        fields = "__all__"

class practice_form(forms.ModelForm):
    class Meta:
        model = practice_set
        fields = "__all__"