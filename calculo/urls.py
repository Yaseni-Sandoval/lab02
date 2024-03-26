from django.urls import path
from . import views

app_name = 'calculo'

urlpatterns = [
   # ex: /encuesta/
   path('', views.calculo, name='calculo'),
]