from django import forms
from .model import User 


class UserForm(form.ModelForm) :
    class Meta :
        model = User 
        fields = ['firstname','lastname','phone','email','code','address','role','device','department','office']