from django.shortcuts import render
from django.http import HttpResponse

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
        'posts': posts,
        'total': 111,
    }
    return render(request, 'blog/home.html', context=context)

def about(request):
    return render(request, 'blog/about.html')


def homeOld(request):
    return HttpResponse('You are at Blog Home')


def aboutOld(request):
    return HttpResponse('Blog About')
