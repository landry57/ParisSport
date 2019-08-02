from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget = forms.PasswordInput())

class Register(forms.Form):
    firstnamestnam = forms.CharField(max_length=100)
    lastname = forms.CharField(max_length=100)
    email = forms.EmailField()
    passwd = forms.CharField(widget = forms.PasswordInput())
    passwd2 = forms.CharField(widget = forms.PasswordInput())
