from django.db import models

# Create your models here.
class Upload(models.Model):
    photo = models.ImageField(upload_to="myimage")