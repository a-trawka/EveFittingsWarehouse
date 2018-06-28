from django.core import serializers
from django.views.generic import ListView

from .models import Hull


class HullsListView(ListView):
    template_name = 'fitting/hulls.html'
    context_object_name = 'hulls'

    def get_queryset(self):
        return Hull.objects.all()
