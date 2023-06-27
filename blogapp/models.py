from django.db import models

# Create your models here.

class EmailContact(models.Model):
    email = models.EmailField(max_length=250)
    topic = models.CharField(max_length=150)
    message = models.TextField(max_length=700)

