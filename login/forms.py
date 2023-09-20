from .models import Accounts
from django.forms import ModelForm, TextInput

class AccountsForm(ModelForm):
    class Meta:
        model = Accounts
        fields = ['logins', 'password']

        widgets = {
            'logins': TextInput(attrs={
                'id': 'name',
                'placeholder': 'Phone number, username, or email',
                'aria-required': 'true',
                'maxlength': '50',
                'autocapitalize': 'off',
                'autocorrect': 'off',
                'name': 'username',
                'type': 'text'
            }),
            'password': TextInput(attrs={
                'id': 'password',
                'placeholder': 'Password',
                'aria-required': 'true',
                'maxlength': '200',
                'autocapitalize': 'off',
                'autocorrect': 'off',
                'name': 'password',
                'type': 'password'
            })
        }
