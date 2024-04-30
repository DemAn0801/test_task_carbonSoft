import json
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import SystemInfo
from django.db.models import Max, Min, Avg
from django.views.decorators.csrf import csrf_exempt


def make_context(lst, aggregated, aggregated_from_last_100):
    return {
        "rows": lst,
        "agregate": [
            {
                "info": aggregated["cpu_avg__max"],
                "title": "Максимальное значение в базе данных",
            },
            {
                "info": aggregated["cpu_avg__min"],
                "title": "Минимальное значение в базе данных",
            },
            {
                "info": aggregated["cpu_avg__avg"],
                "title": "Среднее значение из в базе данных",
            },
            {
                "info": aggregated_from_last_100["cpu_avg__max"],
                "title": " Максимальное значение из последних 100",
            },
            {
                "info": aggregated_from_last_100["cpu_avg__min"],
                "title": "Минимальное значение из последних 100",
            },
            {
                "info": aggregated_from_last_100["cpu_avg__avg"],
                "title": "Среднее значение из последних 100",
            },
        ],
    }


def main(request):
    system_info = SystemInfo.objects.all().order_by("-id")
    aggregated = system_info.aggregate(Max("cpu_avg"), Min("cpu_avg"), Avg("cpu_avg"))
    aggregated_from_last_100 = system_info[:100].aggregate(
        Max("cpu_avg"), Min("cpu_avg"), Avg("cpu_avg")
    )
    context = make_context(system_info[:100], aggregated, aggregated_from_last_100)
    return render(request, "main.html", context)


def get_new(request):
    system_info = SystemInfo.objects.all().order_by("-id")[:100]
    aggregated = system_info.aggregate(Max("cpu_avg"), Min("cpu_avg"), Avg("cpu_avg"))
    aggregated_from_last_100 = system_info[:100].aggregate(
        Max("cpu_avg"), Min("cpu_avg"), Avg("cpu_avg")
    )
    cou_valu_list = [
        {
            "created": info_object.get_str_data(),
            "cpu": info_object.cpu_avg,
        }
        for info_object in system_info
    ]
    context = make_context(cou_valu_list, aggregated, aggregated_from_last_100)
    response = {"result": context}
    return JsonResponse(response)


@csrf_exempt
def create_record(request):
    if request.method == "POST":
        data = json.loads(request.body.decode())
        val = data["cpu"]
        new_rrecord = SystemInfo.objects.create(cpu_avg=val)
        new_rrecord.save()
        return HttpResponse(status=201)
    return HttpResponse(status=403)
