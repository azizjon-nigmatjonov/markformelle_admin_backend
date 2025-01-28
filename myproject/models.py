from django.db import models

class User(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    name = models.CharField(max_length=255, null=True, blank=True)
    # Add more fields as necessary

    def __str__(self):
        return self.email


class Roll(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    # Add more fields as necessary

    def __str__(self):
        return self.name
