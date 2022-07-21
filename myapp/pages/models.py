from django.db import models

# Create your models here.
class Page(models.Model):
    title = models.CharField(max_length=30)
    permalink = models.CharField(max_length=12,unique=True)
    update_date = models.DateTimeField('Last Updated')
    bodytext = models.TextField(default="this is by-default", blank=True)

    def __str__(self):
        return self.title

class Contactform(models.Model):
    yourname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    subject = models.CharField(max_length=100)
    message = models.TextField(max_length=500, default="type your message")

    def __str__(self):
        return self.yourname
