from django.urls import path

from . import views

urlpatterns = [
    path('hulls', views.HullsListView.as_view())
]