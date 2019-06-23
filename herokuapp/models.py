from django.db import models

# Create your models here.
# https://docs.djangoproject.com/en/2.2/ref/models/fields/

class User(models.Model):
    id = models.AutoField
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    phone = models.IntegerField(default=0)
    address = models.CharField(max_length=200)

    def phuong(self):
        return self.username

