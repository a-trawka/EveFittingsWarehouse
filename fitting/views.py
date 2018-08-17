from json import loads

from django.core.serializers import serialize
from django.http import JsonResponse
from django.shortcuts import get_list_or_404
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View

from .models import Hull, Module


@method_decorator(csrf_exempt, name='dispatch')
class CRUDView(View):
    http_method_names = ['get', 'post', 'patch', 'delete']
    model = None

    def get(self, *args, **kwargs):
        if 'pk' in kwargs:
            serialized = serialize('json', get_list_or_404(self.model, pk=kwargs['pk']))
        else:
            serialized = serialize('json', get_list_or_404(self.model))
        return JsonResponse(loads(serialized), safe=False)


class HullView(CRUDView):
    http_method_names = ['get', ]
    model = Hull


class ModuleView(CRUDView):
    http_method_names = ['get', ]
    model = Module
