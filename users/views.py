from django.shortcuts import render, redirect
from django.contrib.auth import login
from .models import User

def signup(request):
    if request.method == 'POST':
        user = User.objects.create_user(
            username=request.POST['username'],
            password=request.POST['password'],
            role=request.POST['role']
        )
        login(request, user)
        return redirect('/events/')
    return render(request, 'signup.html')
