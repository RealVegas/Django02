from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('info', views.info, name='info'),
    path('pan_eng', views.pan_eng, name='pan_eng'),
    path('pan_rus', views.pan_rus, name='pan_rus')
]