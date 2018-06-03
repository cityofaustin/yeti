from django.http import HttpResponse, JsonResponse
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


@csrf_exempt
def output(request):
    data = []
    for participant in Participant.objects.all():
        suggestion = []
        for sug in participant.suggestion_set.all():
            suggestion.append({'name_of_component': sug.name_of_component, 'original_text': sug.original_text, 'altered_text': sug.altered_text, 'language': sug.language, 'reason': sug.reason, 'created_at': sug.created_at, 'updated_at': sug.updated_at})

        dic = {'email': participant.email, 'url': participant.url, 'suggestion': suggestion,'created_at': participant.created_at, 'updated_at': participant.updated_at}
        data.append(dic)

    return JsonResponse(data, safe=False)
