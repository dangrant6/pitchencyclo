from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
#from djangouploads import views

urlpatterns = [
    path("", views.index, name='index'),
    path("<int:pitch>", views.pitch_by_num),
    path("<str:pitch>", views.pitch_select,name='pitch_name'),
    path('download',views.download, name='download')
] 

