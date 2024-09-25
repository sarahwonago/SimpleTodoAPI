
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone
from rest_framework.permissions import IsAuthenticated

from .permissions import IsOwner
from .models import Task
from .serializers import TaskSerializer


class TaskListCreateView(APIView):
    """
    API view to create and list tasks for authenticated users.
    
    Methods:
        get: List tasks based on filters.
        post: Create a new task.
    """
  
    permission_classes = [IsAuthenticated, IsOwner]

    def get(self, request):

        """
        Handle GET request to fetch tasks for the authenticated user.
        apply filters if provided for status, priority,.
        """
        tasks = Task.objects.filter(user=request.user)

        # Apply filters
        status_filter = request.query_params.get('status')
        priority_filter = request.query_params.get('priority')
        

        if status_filter:
            tasks = tasks.filter(status=status_filter)
        if priority_filter:
            tasks = tasks.filter(priority=priority_filter)


        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        """
        Handle POST request to create a new task for the authenticated user.
        Ensure the task's due date is in the future.
        """
        serializer = TaskSerializer(data=request.data)

        if serializer.is_valid():
            # checks if due date is in the past
            if serializer.validated_data['due_date'] <= timezone.now():
                return Response(
                    {"error": "Due date cannot be in the past."},
                    status=status.HTTP_400_BAD_REQUEST
                )
            
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TaskDetailView(APIView):
    """
    API view to retrieve, update, and delete a task for authenticated users.
    
    Methods:
        get: Retrieve a specific task.
        put: Update task details.
        delete: Delete a task.
    """
    permission_classes = [IsAuthenticated, IsOwner]

    def get_object(self, pk, user):
        try:
            return Task.objects.get(pk=pk, user=user)
        except Task.DoesNotExist:
            return None

    def get(self, request, pk):
        """
        Handle GET request to retrieve a task.
        """
        task = self.get_object(pk, request.user)
        if task is None:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = TaskSerializer(task)
        return Response(serializer.data)

    def put(self, request, pk):
        """
        Handle PUT request to update a task.
        Ensure that tasks with a passed due date cannot be updated.
        """
        task = self.get_object(pk, request.user)
        if task is None:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if task.is_overdue():
            return Response(
                {"error": "Cannot update a task whose due date has passed."},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = TaskSerializer(task, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        """
        Handle DELETE request to delete a task.
        """
        task = self.get_object(pk, request.user)
        if task is None:
            return Response(status=status.HTTP_404_NOT_FOUND)

        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class TaskAnalyticsView(APIView):
    """
    API view to provide task analytics for authenticated users.
    
    Methods:
        get: Retrieve task statistics.
    """
    permission_classes = [IsAuthenticated, IsOwner]

    def get(self, request):
        """
        Handle GET request to provide analytics on completed, pending, and overdue tasks.
        """
        user = request.user
        completed_tasks = Task.objects.filter(user=user, status='done').count()
        pending_tasks = Task.objects.filter(user=user, status='pending').count()
        overdue_tasks = Task.objects.filter(user=user, due_date__lt=timezone.now()).count()

        data = {
            'completed_tasks': completed_tasks,
            'pending_tasks': pending_tasks,
            'overdue_tasks': overdue_tasks,
        }
        return Response(data)

class BulkTaskUpdateView(APIView):
    """
    API view to update multiple tasks' status in bulk.
    
    Methods:
        put: Update status for multiple tasks.
    """
    permission_classes = [IsAuthenticated, IsOwner]

    def put(self, request):
        task_ids = request.data.get('task_ids')
        new_status = request.data.get('status')

        if task_ids and new_status:
            tasks = Task.objects.filter(id__in=task_ids, user=request.user)
            tasks.update(status=new_status)
            return Response({"message": "Tasks updated successfully."}, status=status.HTTP_200_OK)
        return Response({"error": "Invalid input."}, status=status.HTTP_400_BAD_REQUEST)
    

# Task History
# time tracking
# task analytics and insights
# endpoints for tags : crud
# endpoints for starting and ending a task
# endpoint for viewing archived tasks

# Business Logic:
# After marking a task as "done" or when the due date passes, check if the task is recurring.
# If the task is recurring, create a new task instance with a new due_date based on the recurrence frequency.
# Example: If the recurrence is daily, increment the due_date by 1 day and save it as a new task.
