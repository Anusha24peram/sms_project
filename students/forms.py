from django import forms
from .models import Student, Enrollment

class StudentForm(forms.ModelForm):
    dob = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}), required=False)
    class Meta:
        model = Student
        fields = ['first_name','last_name','email','roll_number','dob','gender','photo']

class EnrollmentForm(forms.ModelForm):
    class Meta:
        model = Enrollment
        fields = ['student','course','marks']
