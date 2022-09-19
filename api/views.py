from django.shortcuts import render
from rest_framework.views import APIView
from reminder.models import Reminder , Message
# Create your views here.
from .serializers import ReminderSerializer , MessageSerializer
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
import datetime


class ReminderApi(APIView):

    """
    A class used to represent an API view 
    Prints the reminder message and you want to create or delete in reminder
    """

    def get(self, request):
        """"
        in this function handle get method
        return message
        """
        
        try:
            
            reminder = Reminder.objects.get(date_message=datetime.date.today())
            reminder = reminder.text_reminder.all()
            data = MessageSerializer(reminder , many = True).data
            return Response(data)


                
        except:

            data = {
                "message" : 'today you dont have any reminder'
            }
            return JsonResponse(data)


    def post(self, request, format=None):

        """"
        handle post request to create new reminder
        
        """
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
        




class MessageAPI(APIView):


    def post(self, request, pk):

        """"
        handle post request to create new messages
        
        """
        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



        

