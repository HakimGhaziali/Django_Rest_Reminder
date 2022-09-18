from django.db import models
# Create your models here.
from django.contrib.auth import get_user_model


class Reminder(models.Model):

    title = models.CharField(max_length=50)
    content = models.TextField()
    date_reminder = models.DateField()
    date_create = models.DateTimeField(auto_now=True)
    date_message = models.DateField()
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE , related_name='users')




class Message(models.Model):

    reminder = models.ForeignKey(Reminder ,on_delete=models.CASCADE , related_name='t_reminder' )
    heading = models.CharField(max_length=100)
