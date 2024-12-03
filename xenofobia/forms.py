# xenofobia/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from xenofobia.models import UserMessage # 替换为你的模型路径

class UserMessageForm(forms.ModelForm):
    class Meta:
        model = UserMessage
        fields = ['message']# 
class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
