

from django.urls import path
from .import views #import all views functions

urlpatterns = [
    #will aoutomaticaly foward to the index
    path('',views.index,name="index"),
    path('delete/<city_name>/', views.delete_city, name='delete_city')
]
