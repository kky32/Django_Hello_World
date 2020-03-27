from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'blog/home.html')

def homeOld(request):
    return HttpResponse('You are at Blog Home')

def about(request):
    return HttpResponse('Blog About')