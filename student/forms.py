from django import forms
from .models import studentmodel
from django.contrib.auth.models import User

class studentform(forms.ModelForm):
    class Meta:
        model = studentmodel
        fields = "__all__"



