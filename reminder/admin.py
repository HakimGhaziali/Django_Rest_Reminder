from django.contrib import admin

from .models import Reminder , Message 

@admin.register(Reminder)
class ReminderAdmin(admin.ModelAdmin):
    list_display = ('title', 'content',)



@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('reminder', 'heading',)

