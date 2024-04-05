from django import forms
from .models import User

class UserForm(forms.ModelForm):
    class Meta:
        model= User
        fields = ['first_name','last_name','department','school','email','phone_num']


 
class RegistrationForm(forms.Form):
    email = forms.EmailField()

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('This email address is already registered.')
        return email