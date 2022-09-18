from django.shortcuts import render
from rest_framework import generics
from reminder.models import Reminder , Message
# Create your views here.
from .serializers import ReminderSerializer

ReminderSerializer

class ReminderApi(generics.ListAPIView):
    
    queryset = Reminder.objects.all()
    serializer_class = ReminderSerializer 
