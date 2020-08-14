from django import forms
from .models import ContactUS


class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUS
        fields = ['first_name', 'last_name', 'email', 'subject', 'message']
    # first_name = forms.CharField(max_length=30, required=True)
    # last_name = forms.CharField(max_length=30, required=True)
    # email = forms.EmailField(required=True)
    # subject = forms.CharField(max_length=100,required=True)
    # message = forms.CharField(widget=forms.Textarea, required=True)
