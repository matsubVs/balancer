from django.urls import path
from .views import *

urlpatterns = [
    path('long/', long_request),
    path('short/', short_request),
]
