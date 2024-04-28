from django import forms

class LoginForm(forms.Form):

    username = forms.CharField(min_length = 3)
    password = forms.CharField(min_length = 4, widget = forms.PasswordInput)

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


class SignupForm(forms.Form):
    username = forms.CharField()
    password1 = forms.CharField(widget = forms.PasswordInput)
    password2 = forms.CharField(widget = forms.PasswordInput)
    profile_image = forms.ImageField()
    short_description = forms.CharField()
    
    # To add CSS style on each field.
    widget = {
          'username' : forms.TextInput(
            attrs = {
                'id' : 'name',
                'class' : 'form-input',
                'type' : 'text' ,
                'name' : 'name',
                'placeholder' : 'Your Name'
            }
        ),
    }
