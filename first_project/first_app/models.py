from django.db import models

class Topic(models.Model):
    top_name = models.CharField(max_length=264, unique=True)

class Webpage(models.Model):
    category = models.ForeignKey(Topic)
name = models.CharField(max_length=264)
    url = models.URLField()
def __str__(self):
        return self.name
