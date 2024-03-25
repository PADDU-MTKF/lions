
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name="home"),
    path('home', views.home,name="home"),
    path('about', views.about,name="about"),
    path('events', views.event,name="event"),
    path('cache', views.updateCache,name="cache"),
]
