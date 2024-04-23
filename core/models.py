# core/models.py

from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=30)
    phone = models.CharField(max_length=10, blank=True, null=True)
    math_marks = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    science_marks = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    english_marks = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    hindi_marks = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    social_science_marks = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    computer_information_marks = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    physics_marks = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    chemistry_marks = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    mathematics_marks = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

    def total_marks(self):
        return self.math_marks + self.science_marks + self.english_marks + self.hindi_marks + self.socialscience_marks + self.computerinformation_marks + self.physics_marks + self.chemistry_marks + self.mathematics_marks


   

    def __str__(self):
        return self.name

    


