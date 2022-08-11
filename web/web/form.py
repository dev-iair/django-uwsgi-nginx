from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from .models import User

class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password',widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation',widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('id','name')

    def clean_password2(self):
        password_first = self.cleaned_data.get('password_first')
        password_second = self.cleaned_data.get('password_second')
        if password_first and password_second and password_first != password_second:
            raise forms.ValidationError("Passwords don't match")
        return password_second

    def save(self,commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password_first"])
        if commit:
            user.save()
        return user

class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('id','name')

    def clean_password(self):
        return self.initial["password"]