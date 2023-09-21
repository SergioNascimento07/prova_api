from django.db import models
from .studentModel import Student
from .subjectModel import Subject

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    due_date = models.DateField()
    completed = models.BooleanField(default=False)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="tasks")  # Many-to-One Relationship with Student
    subjects = models.ManyToManyField(Subject)  # Many-to-Many Relationship with Subjec

    def __str__(self) -> str:
        return self.title