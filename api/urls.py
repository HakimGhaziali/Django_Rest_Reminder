from django.contrib import admin
from django.urls import path , include
from .views import ReminderApi
urlpatterns = [

    path('', ReminderApi.as_view() , name ='reminder_api'),
    path('<int:pk>', ReminderApi.as_view() , name ='reminder_api'),
    

]