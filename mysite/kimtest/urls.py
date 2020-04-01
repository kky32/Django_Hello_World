from django.urls import path
from . import views

urlpatterns = [
    path('', views.kimtest, name='kimtest'),
    path('test2/', views.test2, name='test2'),
    path('kimtest/', views.kimtest, name='kimtest'),
]
