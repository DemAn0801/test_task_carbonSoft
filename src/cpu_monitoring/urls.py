from django.urls import path
from cpu_monitoring.views import main

urlpatterns = [
    path("", main),
]
