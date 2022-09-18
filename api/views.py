from django.shortcuts import render
from rest_framework.views import APIView
from reminder.models import Reminder , Message
# Create your views here.
from .serializers import ReminderSerializer
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
import datetime


class ReminderApi(APIView):

    def get(self, request):

        try:
            
            reminder = Reminder.objects.get(date_message=datetime.date.today())
            data = ReminderSerializer(reminder).data
            return Response(data)

        except:

            data = {
                "message" : 'today you dont have any reminder'
            }
            return JsonResponse(data)


    def post(self, request, format=None):
        serializer = ReminderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request , pk):

        reminder = Reminder.objects.get(pk=pk)
        serializer = ReminderSerializer(reminder , data = request.data , partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

    def delete(self , request , pk):
        reminder = Reminder.objects.get(pk=pk)
        reminder.delete()
        return Response({'message': 'question deleted'})
        




        

