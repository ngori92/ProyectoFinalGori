from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


# Create your models here.
class Avatar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    imagen = models.ImageField(upload_to='imagenes', null=True, blank = True)

    def __str__(self):
        if self.imagen:
            print("\n\n IMAGEN \n\n")
            return f"{settings.MEDIA_URL}{self.imagen}"
        else:
            print(f"\n\n\n {settings.MEDIA_URL}'default_avatar.jpeg' \n\n\n")
            return f"{settings.MEDIA_URL}'default_avatar.jpeg"