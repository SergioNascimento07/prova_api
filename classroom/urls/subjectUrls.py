from django.urls import path
from ..views.subjectViews import SubjectView, SubjectDetailView

subject_urls = [
    path('subjects', SubjectView.as_view(), name='subject-list'),
    path('subjects/<int:pk>', SubjectDetailView.as_view(), name='subject-detail'),
]