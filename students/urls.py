from django.urls import path
from . import views

app_name = 'students'

urlpatterns = [
    path('', views.StudentListView.as_view(), name='student-list'),
    path('student/add/', views.StudentCreateView.as_view(), name='student-add'),
    path('student/<int:pk>/', views.StudentDetailView.as_view(), name='student-detail'),
    path('student/<int:pk>/edit/', views.StudentUpdateView.as_view(), name='student-edit'),
    path('student/<int:pk>/delete/', views.StudentDeleteView.as_view(), name='student-delete'),

    # optional
    path('enrollment/add/', views.EnrollmentCreateView.as_view(), name='enrollment-add'),
]
