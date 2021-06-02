from django import forms
from .models import todo
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class TodoCreateForm(forms.Form):
    task_name=forms.CharField()
    choices=(("completed","completed"),
                ("notcompleted","notcompleted"))
    status=forms.ChoiceField(choices=choices)
    user=forms.CharField()

class TodoUpdateForm(forms.ModelForm):
    class Meta:
        model=todo
        fields='__all__'

class UserRegisterationForm(UserCreationForm):
    class Meta:
        model=User
        fields=["first_name","email","username","password1","password2"]

class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField()
