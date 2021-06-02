from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.contrib.auth.models import User
from django.forms import TextInput


class AuthUserForm(AuthenticationForm, forms.ModelForm): #authentication
    class Meta:
        model = User
        fields = ['username', 'password']


class RegisterUserForm(forms.ModelForm): #register
    class Meta:
        model = User
        fields = ['username', 'password']

        widgets = {
            "username": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Имя '
            }),
            'password': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Пароль'
            })

        }


    def save(self, commit=True): #hashingn passwd
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user