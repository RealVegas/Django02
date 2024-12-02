from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('second', views.second, name='second page'),
    path('third', views.third, name='third page'),
    path('forth', views.forth, name='forth page'),
    path('fifth', views.fifth, name='fifth page')
]