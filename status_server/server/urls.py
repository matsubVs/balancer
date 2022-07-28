from .views import *
from django.urls import path

urlpatterns = [
	path('status/', StatusResponseView.as_view()),
]