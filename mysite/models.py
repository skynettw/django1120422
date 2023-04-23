from django.db import models

class News(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    source = models.CharField(max_length=50)
    pdate = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title

class BodyInfo(models.Model):
    name = models.CharField(max_length=50)
    height = models.PositiveIntegerField()
    weight = models.PositiveIntegerField()
    def __str__(self):
        return self.name
