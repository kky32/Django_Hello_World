from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterFormCustom
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegisterFormCustom(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created. You may login now {username}.')
            return redirect('/login')
    else:
        form = UserRegisterFormCustom()

    context = {
        'form': form,

    }
    return render(request, 'users/register.html', context=context)

@login_required()
def profile(request):
    return render(request, 'users/profile.html')