from datetime import datetime, date
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.http import HttpResponse

from django.views.generic import ListView, DetailView, CreateView

posts = [
    {
        'author': 'Kim',
        'title': 'Blog Post 1',
        'content': 'First Post content',
        'date_posted': 2020,
    },
    {
        'author': 'Kim2',
        'title': 'Blog Post 2',
        'content': 'Second Post content',
        'date_posted': 2019,
    },
]


def home(request):
    context = {
        'title': 'Title from context',
        'posts': Post.objects.all(),
        'today': date.today().strftime("%Y-%m-%d"),
        'now': datetime.now().strftime("%Y-%m-%d %H:%M %p"),
        'total': len(posts),
        'test_total': len(posts),
        'test_post': posts[0]['author'],
        'test_len': len(Post.objects.all()),
        'test_now': datetime.now().strftime("%Y-%m-%d %I:%M %p")
    }
    return render(request, 'blog/home.html', context=context)


def about(request):
    return render(request, 'blog/about.html')


def homeOld(request):
    return HttpResponse('You are at Blog Home')


def aboutOld(request):
    return HttpResponse('Blog About')


# Example of class based views
class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_created']


class PostDetailView(DetailView):
    model = Post


# We can't use decorators on class
# Use LoginRequiredMixin class to inherit
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content', ]

    # Overwrite parent method
    def form_valid(self, form):
        form.instance.author = self.request.user
        # Will be run on parent class with author
        return super().form_valid(form)
