from django.urls import path
from cpu_monitoring.views import main, get_new

urlpatterns = [
    path("", main), 
    path("get_new/", get_new)
]
