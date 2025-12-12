from django.db import models
from django.urls import reverse

class Course(models.Model):
    name = models.CharField(max_length=120)
    code = models.CharField(max_length=20, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name} ({self.code})"

class Student(models.Model):
    GENDER_CHOICES = [('M','Male'), ('F','Female'), ('O','Other')]
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    email = models.EmailField(unique=True)
    roll_number = models.CharField(max_length=30, unique=True)
    dob = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True)
    photo = models.ImageField(upload_to='student_photos/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['roll_number', 'last_name']

    def __str__(self):
        return f"{self.roll_number} - {self.first_name} {self.last_name}"

    def get_absolute_url(self):
        return reverse('students:student-detail', kwargs={'pk': self.pk})

class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='enrollments')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='enrollments')
    marks = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)  # e.g. 95.50
    enrolled_on = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = ('student', 'course')

    def __str__(self):
        return f"{self.student} in {self.course}"
