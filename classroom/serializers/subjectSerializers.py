from rest_framework import serializers
from ..models.subjectModel import Subject

# Define a serializer class for the 'Subject' model
class SubjectSerializer(serializers.ModelSerializer):
    # Meta class defines the model and fields to be serialized
    class Meta:
        # Specify the model to be used for serialization (Subject model in this case)
        model = Subject
        # Use '__all__' to include all fields from the model in the serialization
        fields = '__all__'