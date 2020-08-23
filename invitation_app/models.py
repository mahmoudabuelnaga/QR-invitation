import os
import shutil
import uuid
from os import path
from xml.dom import minidom
import qrcode
import qrcode.image.svg
import simplejson
import json
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.files.base import ContentFile
from django.core.files.storage import FileSystemStorage
from django.db import models
from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver
from django.utils import timezone
from crum import get_current_user
from django.conf import settings
from django.forms import EmailField
from django_countries.fields import CountryField


def event_directory_path(instance, filename):
    return 'event_id_{0}/{1}'.format(instance.id, filename)


def event_directory_path_for_guest_svg(instance, filename):
    return 'event_id_{0}/svg/{1}'.format(instance.event_id.id, filename)


def event_directory_path_for_guest_image(instance, filename):
    return 'event_id_{0}/image/{1}'.format(instance.event_id.id, filename)


def event_directory_path_for_guest_state(instance, filename):
    return 'event_id_{0}/state/{1}'.format(instance.event_id.id, filename)


# class UserCreationForm(UserCreationForm):
#     email = EmailField(label=("Email address"),
#                        required=True, help_text=("Required."))

#     class Meta:
#         model = User
#         fields = ("username", "email", "password1", "password2")

#     def clean_email(self):
#         email = self.cleaned_data['email'].lower()
#         r = User.objects.filter(email=email)
#         if r.count():
#             raise ValidationError("Email already exists")
#         return email

#     def save(self, commit=True):
#         user = super(UserCreationForm, self).save(commit=False)
#         user.email = self.cleaned_data["email"]
#         print(self.cleaned_data["email"])
#         if commit:
#             user.save()
#         return user


class Country(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class City(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Event_Type(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='our-events')

    def __str__(self):
        return self.name


class OverwriteStorage(FileSystemStorage):
    def get_available_name(self, name, max_length=None):
        if self.exists(name):
            os.remove(os.path.join(settings.MEDIA_ROOT, name))
        return name


class Event(models.Model):
    event_name = models.CharField(max_length=100)
    country = CountryField(
        blank_label='(select country)', null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    event_type = models.ForeignKey(Event_Type, on_delete=models.CASCADE)
    image = models.FileField(storage=OverwriteStorage(
    ), upload_to=event_directory_path, null=True, blank=True)
    image_state = models.FileField(storage=OverwriteStorage(
    ), upload_to=event_directory_path, null=True, blank=True)
    barcode = models.UUIDField(null=True)
    svg = models.FileField(upload_to=event_directory_path)
    is_state_update = models.BooleanField(default=True)
    event_date = models.DateTimeField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    # def __str__(self):
    #     return self.event_name + ' Id is : ' + str(self.id)

    def save(self, *args, **kwargs):
        user = get_current_user()
        if not self.id:
            self.user_id = user
            self.created_at = timezone.now()
            barcode = uuid.uuid4()
            self.barcode = barcode
        return super(Event, self).save(*args, **kwargs)


@receiver(post_delete, sender=Event)
def submission_delete_event(sender, instance, **kwargs):
    dirctory_path = 'media/event_id_' + str(instance.id)
    if(path.exists(dirctory_path)):
        shutil.rmtree(dirctory_path)


@receiver(post_save, sender=Event)
def submission_save_event(sender, instance, **kwargs):
    if(not instance.image and not instance.image_state):
        file_path = 'media/startup_event/startup_design_state.json'
        with open(file_path) as f:
            json_data = json.load(f)
        json_values = simplejson.dumps(json_data)
        instance.image_state.save(
            'state_for_event_id_' + str(instance.id) + '.json', ContentFile(json_values))
        uid = uuid.uuid4()
        img_data = open('media/startup_event/startup_design_image.png', 'rb')
        instance.image.save(
            'image_for_event_id_' + str(instance.id) + '_' + str(uid) + '.' + 'png', img_data)


@receiver(post_save, sender=Event)
def create_svg_for_event(sender, instance, **kwargs):
    if(not instance.svg):
        factory = qrcode.image.svg.SvgPathImage
        qr_file = ContentFile(
            b'', name='svg_for_event_id_' + str(instance.id) + '.svg')
        qrcode.make(instance.barcode, image_factory=factory).save(qr_file)
        instance.svg = qr_file
        instance.save()
        file_path = 'media/' + str(instance.svg)
        doc = minidom.parse(file_path)
        for path in doc.getElementsByTagName('path'):
            event_svg_d_path = path.getAttribute('d')

        file_path = 'media/' + str(instance.image_state)
        with open(file_path) as f:
            json_data = json.load(f)
        json_data['canvas']['objects'][1]['path'] = event_svg_d_path
        json_values = simplejson.dumps(json_data)
        instance.image_state.save(
            'state_for_event_id_' + str(instance.id) + '.json', ContentFile(json_values))


class Guest(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True,
                          serialize=False, verbose_name='ID')
    event_id = models.ForeignKey(Event, on_delete=models.CASCADE)
    barcode = models.UUIDField(unique=True)
    guest_name = models.CharField(max_length=200, null=True, blank=True)
    svg = models.FileField(upload_to=event_directory_path_for_guest_svg)
    image = models.FileField(storage=OverwriteStorage(
    ), upload_to=event_directory_path_for_guest_image, null=True, blank=True)
    state = models.FileField(storage=OverwriteStorage(
    ), upload_to=event_directory_path_for_guest_state, null=True, blank=True)
    check_in_date = models.DateTimeField(null=True, blank=True)

    # def __str__(self):
    #     return self.guest_name + ' Id is : ' + str(self.id)

    def save(self, *args, **kwargs):
        if not self.id:
            barcode = uuid.uuid4()
            self.barcode = barcode
            super(Guest, self).save(*args, **kwargs)
        return super(Guest, self).save(*args, **kwargs)


@receiver(post_save, sender=Guest)
def create_qr_file(sender, instance, **kwargs):
    if (not instance.svg):
        factory = qrcode.image.svg.SvgPathImage
        qr_file = ContentFile(
            b'', name='svg_for_guest_id_' + str(instance.id) + '.svg')
        qrcode.make(instance.barcode, image_factory=factory).save(qr_file)
        instance.svg = qr_file


@receiver(post_delete, sender=Guest)
def submission_delete_guest(sender, instance, **kwargs):
    instance.image.delete(False)
    instance.svg.delete(False)
    instance.state.delete(False)


class Templates(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True,
                          serialize=False, verbose_name='ID')
    upload = models.FileField(upload_to='uploads/')
    event_image = models.FileField(upload_to='uploads/')
    template_name = models.CharField(max_length=50, null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Templates"

    def save(self, *args, **kwargs):
        user = get_current_user()
        if not self.id:
            self.user_id = user
        return super(Templates, self).save(*args, **kwargs)
