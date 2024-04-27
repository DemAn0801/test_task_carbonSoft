from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def main(request):
    context = {
        "rows" : [
            {
            "id": 1,
            "created": 1111,
            "value": 0.1
            },
            {
            "id": 2,
            "created": 2222,
            "value": 0.2
        }
        ]
    }
    return render(request, "table.html", context )
