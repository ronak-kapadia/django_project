from django.urls import path
from .views import my_fun,my_name

urlpatterns = [
    path('call_my_fun/', my_fun),
    path('call_my_name/', my_name)
]
