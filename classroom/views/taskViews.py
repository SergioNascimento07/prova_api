from rest_framework.views import APIView
from rest_framework.response import Response
from ..models.taskModel import Task
from ..serializers.taskSerializers import TaskSerializer
from rest_framework.exceptions import ValidationError
from rest_framework import status

class TaskView(APIView):
    # Receives a 'request' object as a parameter
    def get(self, request):
        try:
            # Get all Task objects from the database
            tasks = Task.objects.all()
            # Serialize Task objects into JSON format
            serializer = TaskSerializer(tasks, many=True)

            # Check if there are no serialized data
            if serializer.data == []:
                # Return a response with status 200 OK and a message of "Tasks not found"
                return Response({"detail": "Tasks not found", "object": serializer.data}, status=status.HTTP_200_OK)

            # Return a response with status 200 OK and the list of serialized tasks
            return Response({"detail": "Tasks returned successfully", "object": serializer.data}, status=status.HTTP_200_OK)

        except Exception as error:
            # Return a response with status 500 Internal Server Error if an unexpected error occurs
            return Response({"detail": {'error_name': error.__class__.__name__, 'error_cause': error.args}}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # Receives a 'request' object as a parameter
    def post(self, request):
        try:
            # Get data from the request
            data = request.data

            # Data should have the following fields based on the Task model:
            # - 'title': The task's title
            # - 'description': The task's description
            # - 'due_date': The task's due date
            # - 'completed': A flag indicating if the task is completed or not
            # - 'disciplines': The disciplines associated with the task (ManyToMany)

            # Check if no data is sent in the request body
            if not data:
                # Raise a validation exception if no data is sent
                raise ValidationError("No fields are being sent by the request body")

            # Serialize task data and validate it
            task = TaskSerializer(data=data)
            # Check if the data is valid
            task.is_valid(raise_exception=True)
            # Save the task to the database
            task.save()

            # Return a response with status 201 Created and the data of the created task
            return Response({"detail": "Task created successfully", "object": task.data}, status=status.HTTP_201_CREATED)

        except ValidationError as error:
            # Return a response with status 400 Bad Request if a validation error occurs
            return Response({"detail": {'error_name': error.__class__.__name__, 'error_cause': error.args}}, status=status.HTTP_400_BAD_REQUEST)

        except Exception as error:
            # Return a response with status 500 Internal Server Error if an unexpected error occurs
            return Response({"detail": {'error_name': error.__class__.__name__, 'error_cause': error.args}}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class TaskDetailView(APIView):
    # Receives a 'request' object and a 'pk' (primary key) parameter as parameters
    def get(self, request, pk):
        try:
            # Get a Task object by ID (pk)
            task = Task.objects.get(pk=pk)
            # Serialize the Task object into JSON format
            serializer = TaskSerializer(task)

            # Return a response with status 200 OK and the task data
            return Response({"detail": "Task returned successfully", "object": serializer.data}, status=status.HTTP_200_OK)

        except Task.DoesNotExist as error:
            # Return a response with status 404 Not Found if the task is not found
            return Response({"detail": { 'error_name': error.__class__.__name__, 'error_cause': error.args}}, status=status.HTTP_404_NOT_FOUND)

        except Exception as error:
            # Return a response with status 500 Internal Server Error if an unexpected error occurs
            return Response({"detail": {'error_name': error.__class__.__name__, 'error_cause': error.args}}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # Receives a 'request' object and a 'pk' (primary key) parameter as parameters
    def patch(self, request, pk):
        try:
            # Get a Task object by ID (pk)
            task = Task.objects.get(pk=pk)
            # Serialize the Task object with the request data, allowing partial updates
            serializer = TaskSerializer(task, data=request.data, partial=True)

            # Data should have the following fields based on the Task model:
            # - 'title': The task's title
            # - 'description': The task's description
            # - 'due_date': The task's due date
            # - 'completed': A flag indicating if the task is completed or not
            # - 'disciplines': The disciplines associated with the task (ManyToMany)

            # Check if the data is valid
            serializer.is_valid(raise_exception=True)
            # Save the task to the database
            serializer.save()
            # Return a response with status 201 Created and the data of the updated task
            return Response({"detail": "Task updated successfully", "object": serializer.data}, status=status.HTTP_201_CREATED)

        except ValidationError as error:
            # Return a response with status 400 Bad Request if a validation error occurs
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Task.DoesNotExist as error:
            # Return a response with status 404 Not Found if the task is not found
            return Response({"detail": { 'error_name': error.__class__.__name__, 'error_cause': error.args}}, status=status.HTTP_404_NOT_FOUND)

        except Exception as error:
            # Return a response with status 500 Internal Server Error if an unexpected error occurs
            return Response({"detail": {'error_name': error.__class__.__name__, 'error_cause': error.args}}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # Receives a 'request' object and a 'pk' (primary key) parameter as parameters
    def put(self, request, pk):
        try:
            # Get a Task object by ID (pk)
            task = Task.objects.get(pk=pk)
            # Serialize the Task object with the request data, replacing all fields
            serializer = TaskSerializer(task, data=request.data)

            # Data should have the following fields based on the Task model:
            # - 'title': The task's title
            # - 'description': The task's description
            # - 'due_date': The task's due date
            # - 'completed': A flag indicating if the task is completed or not
            # - 'disciplines': The disciplines associated with the task (ManyToMany)

            # Check if the data is valid
            serializer.is_valid(raise_exception=True)
            # Save the task to the database
            serializer.save()
            # Return a response with status 201 Created and the data of the updated task
            return Response({"detail": "Task updated successfully", "object": serializer.data}, status=status.HTTP_201_CREATED)

        except ValidationError as error:
            # Return a response with status 400 Bad Request if a validation error occurs
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Task.DoesNotExist as error:
            # Return a response with status 404 Not Found if the task is not found
            return Response({"detail": { 'error_name': error.__class__.__name__, 'error_cause': error.args}}, status=status.HTTP_404_NOT_FOUND)

        except Exception as error:
            # Return a response with status 500 Internal Server Error if an unexpected error occurs
            return Response({"detail": {'error_name': error.__class__.__name__, 'error_cause': error.args}}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    def delete(self, request, pk):
        try:
            # Get a Subject object by ID (pk) and delete it
            task = Task.objects.get(pk=pk)
            task.delete()
            # Return a response with status 200 OK indicating that the subject has been deleted successfully
            return Response({"detail": "Subject deleted successfully"}, status=status.HTTP_200_OK)
        
        except Task.DoesNotExist as error:
            # Return a response with status 404 Not Found if the subject is not found
            return Response({"detail": { 'error_name': error.__class__.__name__, 'error_cause': error.args}}, status=status.HTTP_404_NOT_FOUND)
    
        except Exception as error:
            # Return a response with status 500 Internal Server Error if an unexpected error occurs
            return Response({"detail": {'error_name': error.__class__.__name__, 'error_cause': error.args}}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)