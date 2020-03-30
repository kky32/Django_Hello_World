from django.shortcuts import render
from .models import Employee

# Create your views here.
def kimtest(request):

    kim = Employee('Abc', 'Xyz', 123)

    context = {
        'test': 'Random string goes here',
        'kim' : kim.fullInfo()
    }
    return render(request, 'kimtest/test.html', context)



