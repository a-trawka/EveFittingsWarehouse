from json import loads

from django.core.serializers import serialize
from django.http import JsonResponse
from django.shortcuts import get_list_or_404
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View

from .models import Hull


@method_decorator(csrf_exempt, name='dispatch')
class HullView(View):
    http_method_names = ['get', 'post', 'patch', 'delete']

    def get(self, *args, **kwargs):
        if 'pk' in kwargs:
            serialized = serialize('json', get_list_or_404(Hull, pk=kwargs['pk']))
        else:
            serialized = serialize('json', get_list_or_404(Hull))
        return JsonResponse(loads(serialized), safe=False)


