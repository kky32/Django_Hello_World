from datetime import datetime, date
# from .models import Post
from . import models
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render
from django.http import HttpResponse

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

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
        'posts': models.Post.objects.all(),
        'today': date.today().strftime("%Y-%m-%d"),
        'now': datetime.now().strftime("%Y-%m-%d %H:%M %p"),
        'total': len(posts),
        'test_total': len(posts),
        'test_post': posts[0]['author'],
        'test_len': len(models.Post.objects.all()),
        'test_now': datetime.now().strftime("%Y-%m-%d %I:%M %p"),

        'total_posts': models.Post.objects.all().count,
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
    model = models.Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    paginate_by = 2
    ordering = ['-date_modified']


class PostDetailView(DetailView):
    model = models.Post


# We can't use decorators on class
# Use LoginRequiredMixin class to inherit
class PostCreateView(LoginRequiredMixin, CreateView):
    model = models.Post
    fields = ['title', 'content', ]

    # Overwrite parent method
    # Getting current user into form.instance.author (post.author)
    def form_valid(self, form):
        form.instance.author = self.request.user
        # Will be run on parent class with author
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = models.Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # Prevent other users from updating other people's post
    def test_func(self):
        this_post = self.get_object()
        if this_post.author == self.request.user:
            return True
        else:
            return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = models.Post
    success_url = '/profile'

    # Prevent other users from deleting your post
    def test_func(self):
        this_post = self.get_object()
        if this_post.author == self.request.user:
            return True
        else:
            return False
