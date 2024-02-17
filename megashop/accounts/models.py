from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.CharField(max_length=254, blank=True, null=False)
    address = models.CharField(max_length=255, blank=True, null=False)

    def __str__(self):
        return self.user.username
