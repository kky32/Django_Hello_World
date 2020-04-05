from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('post/all/', views.PostListView.as_view(), name='postListView'),
    path('post/new/', views.PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),
    path('post/<str:username>/', views.PostListViewByUser.as_view(), name='posts-by-user'),
    path('about/', views.about, name='blog-about'),
]