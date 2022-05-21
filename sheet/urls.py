from django.urls import path
from .views import *


urlpatterns = [
    path('', GoogleApi.as_view(), name='index'),
]