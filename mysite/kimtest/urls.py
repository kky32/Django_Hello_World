from django.urls import path
from . import views

urlpatterns = [
    path('', views.kimtest, name='kimtest'),
    path('kimtest/', views.kimtest, name='kimtest'),
]
