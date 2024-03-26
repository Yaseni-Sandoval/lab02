from django.urls import path
from . import views

app_name = 'calculavol'

urlpatterns = [
    path('', views.calculavol, name='calculavol'),
]