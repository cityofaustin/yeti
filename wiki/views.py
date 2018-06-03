from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt
from .models import Suggestion, Participant


@csrf_exempt
def index(request):
    json_data = json.loads(request.body)

    p = Participant(email=json_data["email"], url=json_data["url"])
    p.save()
    print(f'New {p}')

    for item in json_data["suggestions"]:
        s = Suggestion(participant=p, **item)
        s.save()
        print(f'New {s}')

    return HttpResponse(json.dumps(json_data))
