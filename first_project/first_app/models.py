from django.db import models

class User(models.Model):
    name = models.CharField(max_length=264)
    last_name = models.CharField(max_length=264)
    email = models.EmailField(max_length=254,unique=True)
