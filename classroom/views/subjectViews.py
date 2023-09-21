from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models.subjectModel import Subject
from ..serializers.subjectSerializers import SubjectSerializer
from rest_framework.serializers import ValidationError
from rest_framework import status

class SubjectView(APIView):
    # Receives a 'request' object as a parameter
    def get(self, request):
        try:
            # Get all Subject objects from the database
            subjects = Subject.objects.all()
            # Serialize Subject objects into JSON format
            serializer = SubjectSerializer(subjects, many=True)

            # Check if there are no serialized data
            if serializer.data == []:
                # Return a response with status 200 OK and a message of "Subjects not found"
                return Response({"detail": "Subjects not found", "object": serializer.data}, status=status.HTTP_200_OK)
            
            # Return a response with status 200 OK and the list of serialized subjects
            return Response({"detail": "Subjects returned successfully", "object": serializer.data}, status=status.HTTP_200_OK)
        
        except Exception as error:
            # Return a response with status 500 Internal Server Error if an unexpected error occurs
            return Response({"detail": { 'error_name': error.__class__.__name__, 'error_cause': error.args}}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # Receives a 'request' object as a parameter
    def post(self, request):
        try:
            # Get data from the request
            data = request.data

            # Data should have the following parameters based on the Subject model:
            # - 'name': The subject's name
            # - 'description': The subject's description

            # Check if no data is sent in the request body
            if not data:
                # Raise a validation exception if no data is sent
                raise ValidationError("No fields are being sent by the request body")
            
            # Serialize subject data and validate it
            subject = SubjectSerializer(data=data)
            # Check if the data is valid
            subject.is_valid(raise_exception=True)
            # Save the subject to the database
            subject.save()

            # Return a response with status 201 Created and the data of the created subject
            return Response({"detail": "Subject created successfully", "object": subject.data}, status=status.HTTP_201_CREATED)
                
        except ValidationError as error:
            # Return a response with status 400 Bad Request if a validation error occurs
            return Response({"detail": {'error_name': error.__class__.__name__, 'error_cause': error.args}}, status=status.HTTP_400_BAD_REQUEST)
        
        except Exception as error:
            # Return a response with status 500 Internal Server Error if an unexpected error occurs
            return Response({"detail": {'error_name': error.__class__.__name__, 'error_cause': error.args}}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class SubjectDetailView(APIView):
    # Receives a 'request' object and a 'pk' (primary key) parameter as parameters
    def get(self, request, pk):
        try:
            # Get a Subject object by ID (pk)
            subject = Subject.objects.get(pk=pk)
            # Serialize the Subject object into JSON format
            serializer = SubjectSerializer(subject)

            # Return a response with status 200 OK and the subject data
            return Response({"detail": "Subject returned successfully", "object": serializer.data}, status=status.HTTP_200_OK)
        
        except Subject.DoesNotExist as error:
            # Return a response with status 404 Not Found if the subject is not found
            return Response({"detail": { 'error_name': error.__class__.__name__, 'error_cause': error.args}}, status=status.HTTP_404_NOT_FOUND)

        except Exception as error:
            # Return a response with status 500 Internal Server Error if an unexpected error occurs
            return Response({"detail": {'error_name': error.__class__.__name__, 'error_cause': error.args}}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # Receives a 'request' object and a 'pk' (primary key) parameter as parameters
    def patch(self, request, pk):
        try:
            # Get a Subject object by ID (pk)
            subject = Subject.objects.get(pk=pk)
            # Serialize the Subject object with the request data, allowing partial updates
            serializer = SubjectSerializer(subject, data=request.data, partial=True)

            # Data should have the following parameters based on the Subject model:
            # - 'name': The subject's name
            # - 'description': The subject's description

            # Check if the data is valid
            serializer.is_valid(raise_exception=True)
            # Save the subject to the database
            serializer.save()
            # Return a response with status 201 Created and the data of the updated subject
            return Response({"detail": "Subject updated successfully", "object": serializer.data}, status=status.HTTP_201_CREATED)
        
        except ValidationError as error:
            # Return a response with status 400 Bad Request if a validation error occurs
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        except Subject.DoesNotExist as error:
            # Return a response with status 404 Not Found if the subject is not found
            return Response({"detail": { 'error_name': error.__class__.__name__, 'error_cause': error.args}}, status=status.HTTP_404_NOT_FOUND)

        except Exception as error:
            # Return a response with status 500 Internal Server Error if an unexpected error occurs
            return Response({"detail": {'error_name': error.__class__.__name__, 'error_cause': error.args}}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # Receives a 'request' object and a 'pk' (primary key) parameter as parameters
    def put(self, request, pk):
        try:
            # Get a Subject object by ID (pk)
            subject = Subject.objects.get(pk=pk)
            # Serialize the Subject object with the request data, replacing all fields
            serializer = SubjectSerializer(subject, data=request.data)

            # Data should have the following parameters based on the Subject model:
            # - 'name': The subject's name
            # - 'description': The subject's description

            # Check if the data is valid
            serializer.is_valid(raise_exception=True)
            # Save the subject to the database
            serializer.save()
            # Return a response with status 201 Created and the data of the updated subject
            return Response({"detail": "Subject updated successfully", "object": serializer.data}, status=status.HTTP_201_CREATED)
        
        except ValidationError as error:
            # Return a response with status 400 Bad Request if a validation error occurs
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        except Subject.DoesNotExist as error:
            # Return a response with status 404 Not Found if the subject is not found
            return Response({"detail": { 'error_name': error.__class__.__name__, 'error_cause': error.args}}, status=status.HTTP_404_NOT_FOUND)

        except Exception as error:
            # Return a response with status 500 Internal Server Error if an unexpected error occurs
            return Response({"detail": {'error_name': error.__class__.__name__, 'error_cause': error.args}}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # Receives a 'request' object and a 'pk' (primary key) parameter as parameters
    def delete(self, request, pk):
        try:
            # Get a Subject object by ID (pk) and delete it
            subject = Subject.objects.get(pk=pk)
            subject.delete()
            # Return a response with status 200 OK indicating that the subject has been deleted successfully
            return Response({"detail": "Subject deleted successfully"}, status=status.HTTP_200_OK)
        
        except Subject.DoesNotExist as error:
            # Return a response with status 404 Not Found if the subject is not found
            return Response({"detail": { 'error_name': error.__class__.__name__, 'error_cause': error.args}}, status=status.HTTP_404_NOT_FOUND)
    
        except Exception as error:
            # Return a response with status 500 Internal Server Error if an unexpected error occurs
            return Response({"detail": {'error_name': error.__class__.__name__, 'error_cause': error.args}}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)