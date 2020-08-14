from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField
from PIL import Image
import datetime
# Create your models here.

GENDER_CHOICES = (
    ('m', 'male'),
    ('f', 'female')
)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(
        max_length=1, choices=GENDER_CHOICES, default='m', null=True, blank=True)
    country = CountryField(
        blank_label='(select country)', null=True, blank=True)
    pic = models.ImageField(upload_to='profile_pics/',
                            default='profile_pics/User_Avatar.png', blank=True)
    birth_date = models.DateField(
        help_text="yyyy-mm-dd", null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    phone_number = models.CharField(max_length=20,
                                    null=False, blank=False)

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)
        img = Image.open(self.pic.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.pic.path)


@receiver(post_save, sender=User)
def user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
