from django.urls import path 
from .import views

urlpatterns = [
    path('get_office/',views.office,name='office') ,
    path('create_office/',views.create_office,name='create_office')
]
