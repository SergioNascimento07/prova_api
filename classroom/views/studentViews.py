from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models.studentModel import Student
from ..serializers.studentSerializers import StudentSerializer, StudentTasksSerializer
from rest_framework.serializers import ValidationError

class StudentView(APIView):
    # Receives a 'request' object as a parameter
    def get(self, request):
        try:
            # Get all Student objects from the database
            students = Student.objects.all()
            # Serialize Student objects into JSON format
            serializer = StudentSerializer(students, many=True)

            # Check if there are no serialized data
            if serializer.data == []:
                # Return a response with status 200 OK and a message of "Students not found"
                return Response({"detail": "Students not found", "object": serializer.data}, status=status.HTTP_200_OK)
            
            # Return a response with status 200 OK and the list of serialized students
            return Response({"detail": "Students Returned Successfully", "object": serializer.data}, status=status.HTTP_200_OK)
       
        except Exception as error:
            # Return a response with status 500 Internal Server Error if an unexpected error occurs
            return Response({"detail": { 'error_name': error.__class__.__name__, 'error_cause': error.args}}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # Receives a 'request' object as a parameter
    def post(self, request):
        try:
            # Get data from the request
            data = request.data

            # Data should have the following parameters based on the Student model:
            # - 'nome': The student's name
            # - 'email': The student's email address
            
            # Check if no data is sent in the request body
            if not data:
                # Raise a validation exception if no data is sent
                raise ValidationError("No fields are being sent by the request body")
            
            # Serialize student data and validate it
            student = StudentSerializer(data=data)
            # Check if the data is valid
            student.is_valid(raise_exception=True)
            # Save the student to the database
            student.save()

            # Return a response with status 201 Created and the data of the created student
            return Response({"detail": "Student created successfully", "object": student.data}, status=status.HTTP_201_CREATED)
                
        except ValidationError as error:
            # Return a response with status 400 Bad Request if a validation error occurs
            return Response({"detail": {'error_name': error.__class__.__name__, 'error_cause': error.args}}, status=status.HTTP_400_BAD_REQUEST)
        
        except Exception as error:
            # Return a response with status 500 Internal Server Error if an unexpected error occurs
            return Response({"detail": {'error_name': error.__class__.__name__, 'error_cause': error.args}}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class StudentDetailView(APIView):
    # Receives a 'request' object and a 'pk' (primary key) parameter as parameters
    def get(self, request, pk):
        try:
            # Get a Student object by ID (pk)
            student = Student.objects.get(pk=pk)
            # Serialize the Student object into JSON format
            serializer = StudentSerializer(student)

            # Return a response with status 200 OK and the student data
            return Response({"detail": "Student Returned Successfully", "object": serializer.data}, status=status.HTTP_200_OK)
        
        except Student.DoesNotExist as error:
            # Return a response with status 404 Not Found if the student is not found
            return Response({"detail": { 'error_name': error.__class__.__name__, 'error_cause': error.args}}, status=status.HTTP_404_NOT_FOUND)

        except Exception as error:
            # Return a response with status 500 Internal Server Error if an unexpected error occurs
            return Response({"detail": {'error_name': error.__class__.__name__, 'error_cause': error.args}}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # Receives a 'request' object and a 'pk' (primary key) parameter as parameters
    def patch(self, request, pk):
        try:
            # Get a Student object by ID (pk)
            student = Student.objects.get(pk=pk)
            # Serialize the Student object with the request data, allowing partial updates
            serializer = StudentSerializer(student, data=request.data, partial=True)

            # Data should have the following parameters based on the Student model:
            # - 'nome': The student's name
            # - 'email': The student's email address

            # Check if the data is valid
            serializer.is_valid(raise_exception=True)
            # Save the student to the database
            serializer.save()
            # Return a response with status 201 Created and the data of the updated student
            return Response({"detail": "Student updated successfully", "object": serializer.data}, status=status.HTTP_201_CREATED)
        
        except ValidationError as error:
            # Return a response with status 400 Bad Request if a validation error occurs
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        except Student.DoesNotExist as error:
            # Return a response with status 404 Not Found if the student is not found
            return Response({"detail": { 'error_name': error.__class__.__name__, 'error_cause': error.args}}, status=status.HTTP_404_NOT_FOUND)

        except Exception as error:
            # Return a response with status 500 Internal Server Error if an unexpected error occurs
            return Response({"detail": {'error_name': error.__class__.__name__, 'error_cause': error.args}}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # Receives a 'request' object and a 'pk' (primary key) parameter as parameters
    def put(self, request, pk):
        try:
            # Get a Student object by ID (pk)
            student = Student.objects.get(pk=pk)
            # Serialize the Student object with the request data, replacing all fields
            serializer = StudentSerializer(student, data=request.data)

            # Data should have the following parameters based on the Student model:
            # - 'nome': The student's name
            # - 'email': The student's email address

            # Check if the data is valid
            serializer.is_valid(raise_exception=True)
            # Save the student to the database
            serializer.save()
            # Return a response with status 201 Created and the data of the updated student
            return Response({"detail": "Student updated successfully", "object": serializer.data}, status=status.HTTP_201_CREATED)
        
        except ValidationError as error:
            # Return a response with status 400 Bad Request if a validation error occurs
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        except Student.DoesNotExist as error:
            # Return a response with status 404 Not Found if the student is not found
            return Response({"detail": { 'error_name': error.__class__.__name__, 'error_cause': error.args}}, status=status.HTTP_404_NOT_FOUND)

        except Exception as error:
            # Return a response with status 500 Internal Server Error if an unexpected error occurs
            return Response({"detail": {'error_name': error.__class__.__name__, 'error_cause': error.args}}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # Receives a 'request' object and a 'pk' (primary key) parameter as parameters
    def delete(self, request, pk):
        try:
            # Get a Student object by ID (pk) and delete it
            student = Student.objects.get(pk=pk)
            # delete the student
            student.delete()
            # Return a response with status 200 OK indicating that the student has been deleted successfully
            return Response({"detail": "Student deleted successfully"}, status=status.HTTP_200_OK)
        
        except Student.DoesNotExist as error:
            # Return a response with status 404 Not Found if the student is not found
            return Response({"detail": { 'error_name': error.__class__.__name__, 'error_cause': error.args}}, status=status.HTTP_404_NOT_FOUND)
    
        except Exception as error:
            # Return a response with status 500 Internal Server Error if an unexpected error occurs
            return Response({"detail": {'error_name': error.__class__.__name__, 'error_cause': error.args}}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class StudentTaskView(APIView):
    # Receives a 'request' object and a 'pk' (primary key) parameter as parameters
    def get(self, request, pk):
        try:
            # Get a Student object by ID (pk)
            student_tasks = Student.objects.get(pk=pk)
            # Serialize the Student object with all associated tasks
            serializer = StudentTasksSerializer(student_tasks)
            
            # Return a response with status 200 OK and the data of the student's tasks
            return Response({"detail": "Student tasks returned successfully", "object": serializer.data}, status=status.HTTP_200_OK)

        except Student.DoesNotExist as error:
            # Return a response with status 404 Not Found if the student is not found
            return Response({"detail": { 'error_name': error.__class__.__name__, 'error_cause': error.args}}, status=status.HTTP_404_NOT_FOUND)

        except Exception as error:
            # Return a response with status 500 Internal Server Error if an unexpected error occurs
            return Response({"detail": {'error_name': error.__class__.__name__, 'error_cause': error.args}}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            