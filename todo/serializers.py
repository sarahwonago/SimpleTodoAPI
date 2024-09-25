from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Task, Tag

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for the User model.

    Fields:
        id
        username
        email
    """

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email"
        ]


class TagSerializer(serializers.ModelSerializer):
    """
    Serializer for the Tag model.
    """

    class Meta:
        model = Tag
        fields = [
            "id",
            "name"
        ]


class TaskSerializer(serializers.ModelSerializer):
    """
    Serializer for the Task model.

    Fields:
        id(UUID): unique identifier for a task instance.
        title: Title of the task.
        description: Details about the task.
        status: Current status of the task (pending, in_progress, or done).
        priority: Task priority level (low, medium, high).
        due_date: Date when the task is due.
        created_at: Timestamp when the task was created.
        user: User who created the task.
        recurrence: How often the task repeats (none, daily, weekly).
        recurrence_end: when the recurrrence should stop.
        time_spent: Duration user spent on the task.
        start_time: Time the user started the task.
        tags: tags for the task, a task can have more than one tag.
        end_time: Time the user finished the task.
    """

    class Meta:
        model = Task
        fields = '__all__'
        read_only_fields = [
            'user', 'created_at', 'time_spent','start_time', 'end_time'
        ]