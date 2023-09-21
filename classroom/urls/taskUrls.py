from django.urls import path
from ..views.taskViews import TaskView, TaskDetailView

task_urls = [
    path('tasks', TaskView.as_view(), name='task-list'),
    path('tasks/<int:pk>', TaskDetailView.as_view(), name='task-detail'),
]