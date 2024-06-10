from django.urls import path
from .views import office_view

urlpatterns = [
path('call_office_view/',office_view)
]
