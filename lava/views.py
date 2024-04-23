from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import FacRegForm
from core.models import Student

# Accessing the defaulf DB and Asking for
from django.db.models import F, Sum

def registration(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        form = FacRegForm()

        if request.method == 'POST':
            form = FacRegForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('login')


        context = {'form':form}
        return render(request, 'registration.html', {'form':form})


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        if request.method =='POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
            else:
                messages.info(request, 'Incorrect Username Or Password')
        context = {}
        return render(request, 'login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def dashboard(request):

     # Retrieve all students from the database
    students = Student.objects.all()

    # Calculate total marks for each student
    for student in students:
        total_marks = 0
        marks_list = [
            student.math_marks, 
            student.science_marks, 
            student.english_marks, 
            student.hindi_marks, 
            student.social_science_marks, 
            student.computer_information_marks, 
            student.physics_marks, 
            student.chemistry_marks, 
            student.mathematics_marks
        ]
        for mark in marks_list:
            if mark is not None:
                total_marks += mark
        student.total_marks = total_marks
    
    # Sort the students based on total marks in descending order
    students = sorted(students, key=lambda x: x.total_marks, reverse=True)




    # Calculate total marks for each student
   # for student in students:
    #    student.total_marks = student.math_marks + student.science_marks + student.english_marks + student.hindi_marks + student.social_science_marks + student.computer_information_marks + student.physics_marks + student.chemistry_marks + student.mathematics_marks
    
    # Sort the students based on total marks in descending order
   # students = sorted(students, key=lambda x: x.total_marks, reverse=True)

    # Annotate each student object with a calculated total_marks field its a python feature I Didn't knew
    #students = Student.objects.annotate(total_marks=Sum(F('math_marks') + F('science_marks') + F('english_marks') + F('hindi_marks') + F('social_science_marks') + F('computer_information_marks') + F('physics_marks') + F('chemistry_marks') + F('mathematics_marks')))
   # students = Student.objects.all().order_by('-total_marks')




    return render(request, 'dashboard.html', {'students': students})

