from django.shortcuts import render
from .models import SystemInfo

# Create your views here.


def main(request):
    system_info = SystemInfo.objects.all().order_by("-id")[:100]
    context = {"rows": system_info}
    return render(request, "table.html", context)
