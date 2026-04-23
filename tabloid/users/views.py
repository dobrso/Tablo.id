from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login

from .forms import RegistrationForm, ProfileForm
from .models import Profile

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user)
            login(request, user)
            return redirect('users:profile')
    else:
        form = RegistrationForm()

    context = {'form': form}

    return render(request, 'users/register.html', context)

@login_required
def profile(request):
    user_profile = request.user.profile
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('users:profile')
    else:
        form = ProfileForm(instance=request.user.profile)

    context = {
        'profile': user_profile,
        'form': form
    }

    return render(request, 'users/profile.html', context)
