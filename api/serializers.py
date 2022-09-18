from rest_framework import serializers
from reminder.models import Reminder , Message 



class ReminderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reminder
        fields = '__all__'