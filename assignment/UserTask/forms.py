from django import forms
from .models import *

class UserForm(forms.ModelForm):
    class Meta:
        model =  User
        fields = "__all__"
        

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = "__all__"