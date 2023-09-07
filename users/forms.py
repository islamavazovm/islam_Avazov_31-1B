from django import  forms

class RegisterForm(forms.Form):
    username = forms.CharField(min_length=3, max_length=32)
    password_1 = forms.CharField(widget=forms.PasswordInput())
    password_2 = forms.CharField(widget=forms.PasswordInput())

class AuthForm(forms.Form):#
    username = forms.CharField(min_length=3,max_length=32)
    password = forms.CharField(widget=forms.PasswordInput())
