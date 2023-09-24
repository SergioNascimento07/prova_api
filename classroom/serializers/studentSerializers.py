from rest_framework import serializers
from ..models.studentModel import Student
from .taskSerializers import TaskSerializer

# Define a serializer class for the 'Student' model
class StudentSerializer(serializers.ModelSerializer):
    # Meta class defines the model and fields to be serialized
    class Meta:
        # Specify the model to be used for serialization (Student model in this case)
        model = Student
        # Use '__all__' to include all fields from the model in the serialization
        fields = '__all__'

# Define a serializer class for the 'Student' model with tasks
class StudentTasksSerializer(serializers.ModelSerializer):
    # Define a nested serializer 'TaskSerializer' for the 'tasks' field
    tasks = TaskSerializer(many=True, read_only=True)

    # Meta class defines the model and fields to be serialized
    class Meta:
        # Specify the model to be used for serialization (Student model in this case)
        model = Student
        # Include only the 'tasks' field in the serialization
        fields = ['tasks']