"""Defines URL patterns for emotion_detection"""

from django.urls import path

from . import views


app_name = "detection_app"

urlpatterns = [path("", views.home, name="home")]
