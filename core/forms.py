from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Student

class SignUpForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('name', 'email', 'phone', 'math_marks', 'science_marks', 'english_marks', 'hindi_marks', 'social_science_marks','computer_information_marks', 'physics_marks', 'chemistry_marks', 'mathematics_marks')
        widgets = {
            'email': forms.EmailInput(),  # Use EmailInput widget for email field
        }

         

