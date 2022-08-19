from django.urls import path
from . import views

urlpatterns = [
    path('', views.swapi, name='swapi'),
    path('films/', views.films, name='films'),
    path('people/', views.people, name='people'),
]
