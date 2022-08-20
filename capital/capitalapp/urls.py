from django.urls import path
from . import views

urlpatterns = [
    path('', views.swapi, name='swapi'),
    path('films/', views.films, name='films'),
    path('people/', views.people, name='people'),
    path('starships/', views.starships, name='starships'),
    path('vehicles/', views.vehicles, name='vehicles'),
    path('planets/', views.planets, name='planets'),
    path('species/', views.species, name='species'),
    # path('character/', views.character, name='character'),
]
