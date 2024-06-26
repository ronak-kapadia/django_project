from django.urls import path 
from .import views

urlpatterns = [
 path('department_form/',views.department,name='department'),
 path('create_department',views.create_department,name='department'),
]
