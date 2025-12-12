from django.contrib import admin
from .models import Student, Course, Enrollment

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('roll_number','first_name','last_name','email','dob')
    search_fields = ('first_name','last_name','roll_number','email')
    list_filter = ('gender',)
    ordering = ('roll_number',)

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('code','name')
    search_fields = ('code','name')

@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('student','course','marks','enrolled_on')
    search_fields = ('student__first_name', 'student__roll_number', 'course__name')
