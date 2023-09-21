from django.urls import path
from ..views.studentViews import StudentView, StudentDetailView, StudentTaskView

student_urls = [
    path('students', StudentView.as_view(), name='student-list'),
    path('students/<int:pk>', StudentDetailView.as_view(), name='student-detail'),
    path('students/<int:pk>/tasks', StudentTaskView.as_view(), name='student-task-list')
]