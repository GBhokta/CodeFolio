from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserProfileForm

def register(request):
    if request.method == 'POST':
        user_form = UserRegisterForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            login(request, user)
            return redirect('home')
    else:
        user_form = UserRegisterForm()
    return render(request, 'accounts/register.html', {'user_form': user_form})

@login_required
def edit_profile(request):
    if request.method == 'POST':
        profile_form = UserProfileForm(request.POST, request.FILES, instance=request.user.userprofile)
        if profile_form.is_valid():
            profile_form.save()
            return redirect('profile_view')
    else:
        profile_form = UserProfileForm(instance=request.user.userprofile)
    return render(request, 'accounts/edit_profile.html', {'profile_form': profile_form})
def logout_v(request):
    logout(request)
    return redirect('home')