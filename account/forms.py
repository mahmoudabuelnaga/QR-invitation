from django import forms
from django.contrib.auth.forms import UserCreationForm
from django_countries.widgets import CountrySelectWidget
from django.contrib.auth.models import User
from phonenumber_field.formfields import PhoneNumberField
from .models import Profile
import datetime


X = datetime.date.today().year - 100
Y = datetime.date.today().year
YEARS = [i for i in range(X, Y)]


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, required=True)
    last_name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email',
                  'password1', 'password2',)


class ProfileForm(forms.ModelForm):
    birth_date = forms.DateField(widget=forms.SelectDateWidget(years=YEARS,
                                                               attrs={"class": "form-control mb-4", }), required=True)
    phone_number = forms.CharField(max_length=20, required=True)
    city = forms.CharField(max_length=50, required=True)

    class Meta:
        model = Profile
        fields = ('gender', 'country', 'birth_date', 'city', 'phone_number')
        widgets = {'country': CountrySelectWidget(attrs={
            'class': 'custom-select d-block w-100',
        }),
            'phone_number': forms.TextInput(attrs={
                "class": "form-control mb-4",
            }),
            'gender': forms.Select(attrs={
                "class": "form-control mb-4",
            }),
            'city': forms.TextInput(attrs={
                "class": "form-control mb-4",
            }),


        }


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email',)
        widgets = {
            'first_name': forms.TextInput(attrs={
                "class": "form-control mb-4",
            }),
            'last_name': forms.TextInput(attrs={
                "class": "form-control mb-4",
            }),
            'email': forms.TextInput(attrs={
                "class": "form-control mb-4",
            }),
        }


class ProfileUpdateForm(forms.ModelForm):
    birth_date = forms.DateField(widget=forms.SelectDateWidget(years=YEARS,
                                                               attrs={"class": "form-control mb-4", }))
    pic = forms.ImageField()

    class Meta:
        model = Profile
        fields = ('pic', 'birth_date', 'gender', 'country', 'city',
                  'phone_number')
        widgets = {'country': CountrySelectWidget(attrs={
            'class': 'custom-select d-block w-100',
        }),
            'phone_number': forms.TextInput(attrs={
                "class": "form-control mb-4",
            }),
            'gender': forms.Select(attrs={
                "class": "form-control mb-4",
            }),
            'city': forms.TextInput(attrs={
                "class": "form-control mb-4",
            }),

        }
