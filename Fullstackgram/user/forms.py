
from django import forms
from django.contrib.auth.models import User
from user.models import profile

class profileForm(forms.ModelForm):

    website = forms.URLField(max_length= 200, required=False)
    biography =( forms.CharField(max_length= 500, required=True)
    phone-number = forms.CharField(max_length=20, required=False)
    picture = forms.ImageField(required=True)

    class Meta:
        model = profile
        field = ['website', 'biography', 'phone_number', 'picture' ]

class SignupForm(forms.Form):

    username = forms.CharField(min_legth= 4, max_length= 50)
    password = forms.CharField(max_length= 70)

    password_confirmation =  forms.CharField(max_length=70)

    first_name =  forms.CharField(min_legth= 2, max_length=50)
    last_name = forms.CharField(min_legth= 2, max_length=50)

    email = forms.CharFiel(min_legth=10, max_length=70, widget=forms.emailInput())
    