from django.db import models

# Create your models here.



class Reminder(models.Model):

    title = models.CharField(max_length=50)
    content = models.TextField()
    date_reminder = models.DateField()
    date_create = models.DateTimeField(auto_now=True)
    date_message = models.DateField()




class message(models.Model):

    reminder = models.ForeignKey(Reminder ,on_delete=models.CASCADE , related_name='t_reminder' )
    heading = models.CharField(max_length=100)
    