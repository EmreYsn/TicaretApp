from django import forms
from django.forms import ModelForm
from ticaretapp.models import Ticaret

class SignUpForm(forms.Form):
    username_input = forms.CharField(label="Username",max_length=50)

class SignUpModelForm(ModelForm):
    class Meta:
        model = Ticaret
        fields = ["username"]