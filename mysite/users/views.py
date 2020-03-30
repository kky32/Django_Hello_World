from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterFormCustom, UserUpdateForm, ProfileUpdateForm
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
    if request.method == 'POST':
        form_for_user_update = UserUpdateForm(request.POST, instance=request.user)
        form_for_profile_update = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        # IF FORM IS VALID, SAVE DATA
        if form_for_user_update.is_valid() and form_for_profile_update:
            form_for_user_update.save()
            form_for_profile_update.save()

            # PROVIDE FEEDBACK TO USER
            messages.success(request, f'Your account has been updated.')
            return redirect('profile')

    else:
        # GET request
        form_for_user_update = UserUpdateForm(instance=request.user)
        form_for_profile_update = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'form_u': form_for_user_update,
        'form_p': form_for_profile_update,
    }
    return render(request, 'users/profile.html', context=context)

