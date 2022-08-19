from django.urls import path
from . import views

urlpatterns = [
    path('', views.swapi, name='swapi'),
    path('selflink', views.selflink, name='selflink'),
]
