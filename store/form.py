from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm


class HeightWidthForm(forms.ModelForm):
    class Meta():
        model = OrderItem
        fields = ['height', 'width']


class CreateUserForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
            super(CreateUserForm, self).__init__(*args, **kwargs)
            self.fields['username'].label = 'Email:'
    
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        # username = forms.CharField(error_messages={'username_exists': 'fuck oy'})
        error_messages = {
            'username': {
                'username_exists': ("fuckads oy"),
            },
        }
        
        



class CreateCustomerForm(forms.ModelForm):
    class Meta():
        model = Customer
        fields = '__all__'
        exclude = ['user']
