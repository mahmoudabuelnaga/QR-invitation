from django.db import models

# Create your models here.


class About(models.Model):
    image = models.ImageField(upload_to='about/', default='about/700x450.png')
    description = models.TextField()


class Vision(models.Model):
    image = models.ImageField(upload_to='about/', default='vision/700x450.png')
    description = models.TextField()


class ContactUS(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()

    class Meta:
        verbose_name_plural = "Cantact us"

    def __str__(self):
        return f"New contact {self.pk}"
