from django.urls import path 
from .import views

urlpatterns = [
 path('get_device/',views.device,name='device'),
 path('create_device/',views.create_device,name='create_device')
]
