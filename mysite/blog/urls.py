from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('post/all', views.PostListView.as_view(), name='postListView'),
    path('post/new', views.PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>', views.PostDetailView.as_view(), name='post'),
    path('about/', views.about, name='blog-about'),
]