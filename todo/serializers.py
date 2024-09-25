from django.utils import timezone
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

    user = serializers.CharField(source='user.username', read_only=True)

    # Accept tag names as a list of strings instead of nested objects
    tags = serializers.SlugRelatedField(
        many=True,
        slug_field='name',
        queryset=Tag.objects.all()
    )

    class Meta:
        model = Task
        fields = '__all__'
        read_only_fields = [
            'user', 'created_at', 'time_spent','start_time', 'end_time'
        ]
    

    def validate_due_date(self, value):
        """
        Check that the due date is not in the past.
        """
        if value < timezone.now():
            raise serializers.ValidationError("Due date cannot be in the past.")
        return value

    def create(self, validated_data):
        """
        Override create method to handle task and tag creation.
        """
        tags_data = validated_data.pop('tags')
        task = Task.objects.create(**validated_data)

        # Add tags to the task (tags are either created or reused)
        task.tags.set(self._get_or_create_tags(tags_data))

        return task

    def update(self, instance, validated_data):
        """
        Override update method to handle task and tag updates.
        """
        tags_data = validated_data.pop('tags', None)
        instance = super().update(instance, validated_data)

        if tags_data:
            # Clear and reassign tags
            instance.tags.set(self._get_or_create_tags(tags_data))

        return super().update(instance, validated_data)
    
       

    def _get_or_create_tags(self, tags_data):
        """
        Utility function to either get or create tags from the provided list of tag names.
        Returns a list of tag objects.
        """
        tag_objects = []
        for tag_name in tags_data:
            tag, created = Tag.objects.get_or_create(name=tag_name)
            tag_objects.append(tag)
        return tag_objects
