from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("<int:pitch>", views.pitch_by_num),
    path("<str:pitch>", views.pitch_select,name='pitch_name'),
]
