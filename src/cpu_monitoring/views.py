from django.shortcuts import render
from django.http import JsonResponse
from .models import SystemInfo
from django.db.models import Max, Min, Avg


def main(request):
    system_info = SystemInfo.objects.all().order_by("-id")
    aggregated = system_info.aggregate(Max("cpu_avg"), Min("cpu_avg"), Avg("cpu_avg"))
    aggregated_from_last_100 = system_info[:100].aggregate(
        Max("cpu_avg"), Min("cpu_avg"), Avg("cpu_avg")
    )
    context = {
        "rows": system_info[:100],
        "agregate": [
            {
                "id": "max_value",
                "info": aggregated["cpu_avg__max"],
                "title": "Максимальное значение в базе данных",
            },
            {
                "id": "min_value",
                "info": aggregated["cpu_avg__min"],
                "title": "Минимальное значение в базе данных",
            },
            {
                "id": "avg_value",
                "info": aggregated["cpu_avg__avg"],
                "title": "Среднее значение из в базе данных",
            },
            {
                "id": "max_value_from_100",
                "info": aggregated_from_last_100["cpu_avg__max"],
                "title": " Максимальное значение из последних 100",
            },
            {
                "id": "min_value_from_100",
                "info": aggregated_from_last_100["cpu_avg__min"],
                "title": "Минимальное значение из последних 100",
            },
            {
                "id": "avg_value_from_100",
                "info": aggregated_from_last_100["cpu_avg__avg"],
                "title": "Среднее значение из последних 100",
            },
        ],
    }
    return render(request, "table.html", context)


def get_new(request):
    system_info = SystemInfo.objects.all().order_by("-id")[:100]
    # Далее логично былло бы использовать сериализатор, но в в задании DRF не значился
    result = [
        {
            "created": info_object.get_str_data(),
            "cpu": info_object.cpu_avg,
        }
        for info_object in system_info
    ]
    response = {"result": result}
    return JsonResponse(response)
