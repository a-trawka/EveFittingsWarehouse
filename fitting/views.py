from django.views.generic import ListView

from .models import Hull


class HullsIndexView(ListView):
    template_name = 'fitting/hulls.html'
    context_object_name = 'hulls'

    def get_queryset(self):
        return Hull.objects.all()[:5]
