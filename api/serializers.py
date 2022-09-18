from dataclasses import field
from rest_framework import serializers
from reminder.models import Reminder , Message 



class MessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message 
        fields = ('heading','reminder',)



class ReminderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reminder
        fields = '__all__'



