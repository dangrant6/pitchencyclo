from django.urls import path
from . import views

urlpatterns = [
    path("<pitch>", views.pitch_select),
]
