from django.urls import path

from . import views

app_name = 'fitting'

urlpatterns = [
    path('hulls/', views.HullView.as_view(), name='hulls'),
    path('hulls/<int:pk>/', views.HullView.as_view(), name='hull'),

    path('modules/', views.ModuleView.as_view(), name='modules'),
    path('modules/<int:pk>/', views.ModuleView.as_view(), name='module'),
]
