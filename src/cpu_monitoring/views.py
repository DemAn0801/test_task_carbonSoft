from django.shortcuts import render
from django.http import JsonResponse
from .models import SystemInfo


def main(request):
    system_info = SystemInfo.objects.all().order_by("-id")[:100]
    context = {"rows": system_info}
    return render(request, "table.html", context)


def get_new(request):
    system_info = SystemInfo.objects.all().order_by("-id")[:100]
    # Далее логично былло бы использовать сериализатор, но в в задании DRF не значился
    result = [
        {
            "created": o.get_str_data(),
            "cpu": o.cpu_avg,
        }
        for o in system_info
    ]
    response = {"result": result}
    return JsonResponse(response)
