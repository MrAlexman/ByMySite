from django.urls import path
from helloworld.views import *

urlpatterns = [
    path('', index),
    path('test/', test),
]