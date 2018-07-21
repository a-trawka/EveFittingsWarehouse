from django.urls import path

from . import views

app_name = 'fitting'

urlpatterns = [
    path('hulls', views.HullsIndexView.as_view(), name='hulls')
]