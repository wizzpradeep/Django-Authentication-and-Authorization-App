from django import forms
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm

class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(
        label='First name',
        widget=forms.TextInput(
            attrs={'placeholder':'Enter first name','class':'form-control'}
        )
    )
    last_name = forms.CharField(
        label='Last name',
        widget=forms.TextInput(
            attrs={'placeholder':'Enter last name','class':'form-control'}
        )
    )
    username = forms.CharField(
        label='Username',
        widget=forms.TextInput(
            attrs={'placeholder':'Enter username','class':'form-control'}
        )
    )
    email = forms.CharField(
        label='Email',
        widget=forms.EmailInput(
            attrs={'placeholder':'Enter email','class':'form-control'}
        )
    )
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(
            attrs={'placeholder':'Enter password','class':'form-control'}
        )
    )
    password2 = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput(
            attrs={'placeholder':'Retype password','class':'form-control'}
        )
    )

    class Meta:
        model = CustomUser
        fields  = ['first_name','last_name','username','email','password1','password2']
    
class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        label='Email',
        widget=forms.EmailInput(
            attrs={'placeholder':'Enter email','class':'form-control'}
        )
    )
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(
            attrs={'placeholder':'Enter password','class':'form-control'}
        )
    )


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ['first_name','last_name','username','email','date_joined','is_staff','is_active']


