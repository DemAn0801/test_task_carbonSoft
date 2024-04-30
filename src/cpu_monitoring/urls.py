from django.urls import path
from cpu_monitoring.views import main, get_new, create_record

urlpatterns = [
    path("", main),
    path("get_new/", get_new),
    path("post/", create_record),
]
