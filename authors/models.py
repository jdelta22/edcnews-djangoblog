from django.contrib.auth.models import User
from django.db import models


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, default="")
    bio = models.TextField(blank=True)
    email = models.EmailField(max_length=254, default="")
    profile_picture = models.ImageField(upload_to="authors/", blank=True, null=True)

    def __str__(self):
        return self.name
