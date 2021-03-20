from django.db import models

from django.contrib.auth.models import User

# Create your models here.


class AuthTokenApi(models.Model):
    """Model definition for AuthTokenApi."""

    # TODO: Define fields here
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    kind = models.CharField(max_length = 255)
    localId = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)
    idToken = models.TextField()
    registered = models.CharField(max_length = 255)
    refreshToken = models.TextField()
    expiresIn = models.CharField(max_length = 255)


    def __str__(self):
        """Unicode representation of AuthTokenApi."""
        return f"{self.user}"


    # TODO: Define custom methods here
