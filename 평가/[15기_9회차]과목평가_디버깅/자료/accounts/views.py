from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm
from .models import User


def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('todos:index')
    else:
        form = CustomUserCreationForm()
    context = {'form': form}
    return render(request, 'accounts/signup.html', context)


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('todos:index')
    else:
        form = AuthenticationForm()
    context = {'form': form}
    return render(request, 'accounts/login.html', context)


def logout(request):
    auth_logout(request)
    return redirect('todos:index')

@login_required
def profile(request, username):
    user = User.objects.get(username=username)
    context = {'user': user}
    return render(request, 'accounts/profile.html', context)

@login_required
def follow(request, user_pk):
    user = User.objects.get(pk=user_pk)
    if request.user.is_authenticated:
        if request.user != user:
            if request.user in user.followers.all():
                user.followers.remove(request.user)
            else:
                user.followers.add(request.user)
    else:
        return redirect('accounts:login')
    return redirect('todos:index')

@login_required
def following(request, user_pk):
    user = User.objects.get(pk=user_pk)
    context = {'user': user}
    return render(request, 'accounts/following.html', context)

@login_required
def followers(request, user_pk):
    user = User.objects.get(pk=user_pk)
    context = {'user': user}
    return render(request, 'accounts/followers.html', context)
