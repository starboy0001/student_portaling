from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm, StudentForm
from django.contrib import messages
from .models import Student

def signup(request):
    form = SignUpForm()
    if request.user.is_authenticated:
        return redirect('student_info')
    else:

        if request.method == 'POST':
           form = SignUpForm(request.POST)
           if form.is_valid():
              form.save()
              return redirect('signin')

        return render(request, 'signup.html', {'form': form})
    
  
def signin(request):
    if request.user.is_authenticated:
       return redirect('student_info')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('student_info')
            else:
                messages.info(request, 'Incorrect Username Or Password')
        context = {}
        return render(request, 'signin.html', context)


def signout(request):
    logout(request)
    return redirect('signin')
    



@login_required(login_url='signin')
def student_info(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
        else:
            print(form.errors)
            print(form.non_field_errors) 
    else:
        form = StudentForm()
    return render(request, 'student_info.html', {'form': form})

def success(request):
    return render(request, 'success.html')  

# core/views.py
'''
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from .forms import SignUpForm, StudentForm

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('student_info')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})
    
@login_required
def student_info(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = StudentForm()
    return render(request, 'student_info.html', {'form': form})

def success(request):
  #  return render(request, 'success.html')
    return redirect('student_info')  # Redirect back to the student_info view
'''