from django.shortcuts import render, redirect
from .forms import MyUserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import User
from django.contrib.messages import constants
# Create your views here.

def signupUser(request):
    form = MyUserCreationForm()
    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            if User.objects.filter(email=email).exists():
                messages.add_message(request, constants.ERROR, "Email already registered")

            user = form.save(commit=False)
            user.username = user.username.lower()
            user.backend = 'register.backends.EmailBackend'
            user.save()
            login(request, user)
            return redirect("signup")

    return render(request, 'signup.html', context={'form': form, 'messages': messages.get_messages(request)})