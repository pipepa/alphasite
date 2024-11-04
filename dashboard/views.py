
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
# Create your views here.
def home(request):
    return render(request, 'dashboard/home.html')



def loginuser(request):
    if request.method == 'GET':
        return render(request, 'dashboard/authform.html', {'form':AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'dashboard/authform.html', {'form':AuthenticationForm(), 'error':'Username and password did not match'})
        else:
            login(request, user)
            return redirect('currentdasboard')
@login_required
def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('loginuser')
@login_required
def currentdasboard(request):
    return render(request, 'dashboard/dashboard.html')
