from django.urls import include, path
from . import views

urlpatterns = [
    path('weather/', views.events, name="weather"),
]
