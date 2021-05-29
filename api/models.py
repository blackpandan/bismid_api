from django.db import models
from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=250)
    price = models.DecimalField(decimal_places=2, default=0, max_digits=250)
    stock = models.IntegerField(default=0)
    category = models.CharField(max_length=250)
    picture = models.ImageField(default=None, upload_to="static/api/")
    rating = models.IntegerField(default=0)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
