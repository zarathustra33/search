from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core import validators

def check_internal(value):
    if value.split('@')[-1] != 'ocbang.com':
        raise forms.ValidationError('Needs to be company email')



class NewUser(UserCreationForm):
    first_name=forms.CharField(max_length=30,help_text="Required, as it identifies your authentication to the database.")
    last_name=forms.CharField(max_length=30)
    email=forms.EmailField(validators=[check_internal],help_text='Required. Inform a company email address.')
    # password=forms.PasswordInput()
    class Meta():
        model=User
        fields=['username','first_name','last_name','email','password1','password2']
