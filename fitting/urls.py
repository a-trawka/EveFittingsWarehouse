from django.urls import path

from . import views

app_name = 'fitting'

urlpatterns = [
    path('hulls', views.HullsIndexView.as_view(), name='hulls'),
    path('hulls/<int:pk>/', views.HullsDetailView.as_view(), name='hull'),
]