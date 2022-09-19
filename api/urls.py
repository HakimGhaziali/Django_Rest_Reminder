from django.contrib import admin
from django.urls import path , include
from .views import ReminderApi , MessageAPI
urlpatterns = [

    path('reminder', ReminderApi.as_view() , name ='reminder_api'),
    path('reminder/<int:pk>', ReminderApi.as_view() , name ='reminder_detail_api'),
    path('message/<int:pk>', MessageAPI.as_view() , name ='create_message'),



]

