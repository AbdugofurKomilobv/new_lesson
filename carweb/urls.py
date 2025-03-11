from django.urls import path
from .views import *

urlpatterns = [
    path('',car_pages,name='car')
]