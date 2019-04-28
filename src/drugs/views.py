from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from drugs.models import Drugs
from drugs.serializers import DrugsSerializer

@csrf_exempt
def snippet_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        data = JSONParser().parse(request)
        print(data)
        drugs = Drugs.objects.filter(name=data['name'])
        serializer = DrugsSerializer(drugs, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = DrugsSerializer(data=data)
        print(serializer)        
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def snippet_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        drugs = Drugs.objects.get(pk=pk)
    except Drugs.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = DrugsSerializer(drugs)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = DrugsSerializer(drugs, data=data)
        if serializer.is_valid():
            serializer.save()
            print(serializer.data)
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        drugs.delete()
        return HttpResponse(status=204)