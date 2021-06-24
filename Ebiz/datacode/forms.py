from .models import *
from django import forms

class BizForm(forms.ModelForm):
    class Meta:
        model = Biz
        exclude=('doc',)
