from .views import *
from django.urls import path

urlpatterns = [
    path('long/', LongResponseView.as_view()),
	path('short/', ShortResponseView.as_view()),
]