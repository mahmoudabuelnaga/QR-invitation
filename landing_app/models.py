from django.db import models

# Create your models here.


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


class Partner(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='partners-logo')
    url = models.URLField(max_length=200)

    def __str__(self):
        return self.name


class OurClient(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='our-clients')
    description = models.TextField()

    def __str__(self):
        return self.name
