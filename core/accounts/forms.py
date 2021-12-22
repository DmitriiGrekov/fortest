from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model, password_validation
from django.core.exceptions import ValidationError
from django.forms import fields, widgets

from .models import AdvUser


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        fields = ('username', 'password')


class UserRegisterForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',
                                                             'placeholder': 'Логин'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                 'placeholder': 'Пароль'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                  'placeholder': 'Повторите пароль'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',
                                                               'placeholder': 'Имя'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',
                                                              'placeholder': 'Фамилия'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control',
                                                           'placeholder': 'Почта'}))

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        if password1:
            password_validation.validate_password(password1)
        return password1
    
    def clean(self):
        super().clean()
        password = self.cleaned_data.get('password')
        password1 = self.cleaned_data.get('password1')
        user = get_user_model()
        if password1 and password and password != password1:
            errors = {'password1': ValidationError('Введенные пароли не совпадают', 
                                                   code='password_mismathc')}
            raise ValidationError(errors)
        if user.objects.filter(email=self.cleaned_data.get('email')).exists():
            errors = {'email': ValidationError('Введенный email уже существует')}
            raise ValidationError(errors)

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data.get('password1'))
        # user.is_active = False
        # user_reg_ds.send(sender=self.__class__, user=user)
        if commit:
            user.save()
        return user

    class Meta:
        model = AdvUser 
        fields = ('username',
                  'password',
                  'password1',
                  'email',
                  'first_name',
                  'last_name')


