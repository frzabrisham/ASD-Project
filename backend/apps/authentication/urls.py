from django.urls import path
from .views import *

app_name = "authentication"

urlpatterns = [
    path('test/', TestView.as_view())
]