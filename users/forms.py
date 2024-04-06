from django import forms

class LoginForm(forms.Form):

    username = forms.CharField(min_length = 3)
    password = forms.CharField(min_length = 4)

    # To add CSS style on each field
    widget = {
        'username' : forms.TextInput(
            attrs = {
                'class' : 'input100',
                'type' : 'text' ,
                'name' : 'email',
                'placeholder' : 'ID'
            }
        )
        ,
        'password' : forms.PasswordInput(
            attrs = {
                'class' : 'input100',
                'type' : 'password' ,
                'name' : 'pass',
                'placeholder' : 'PASSWORD'
            }
        )
    }
