from django import forms
from django.forms import SelectDateWidget

from .models import Guest, Event

from bootstrap_modal_forms.forms import BSModalForm

# class UserForm(forms.ModelForm):
#     password = forms.CharField(widget=forms.PasswordInput())
#
#     class Meta():
#         model = Guest
#         fields = ('guest_name','email','password')


class EventsForms(forms.ModelForm):
    class Meta():
        model = Event
        fields = '__all__'


# class EventForm(BSModalForm):
#     class Meta:
#         model = Event
#         exclude = ['updated_at']


# class EventPopupForm(BSModalForm):
#     class Meta:
#         model = Event
#         exclude = ['user_id', 'image_state', 'image',
#                    'is_state_update', 'barcode', 'svg']


class GuestPopupForm(BSModalForm):
    class Meta:
        model = Guest
        exclude = ['event_id', 'barcode',
                   'check_in_date', 'svg', 'image', 'state']


class FileUploadForm(forms.Form):
    myfile = forms.FileField()
