import uuid
from django.db import models
from django.contrib.auth import get_user_model

from django.utils import timezone

User = get_user_model()

class Tag(models.Model):
    """
    A model to represent a tag.

    Attributes:
        id(UUID): unique identifier for a tag instance.
        name: Name of the tag.

    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, unique=True)

    def __str__(self) -> str:
        return self.name

class Task(models.Model):
    """
    A model to represent a task.

    Attributes:
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

    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('done', 'Done'),
    ]

    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]


    RECURRING_CHOICES = [
        ('none', 'None'),
        ('daily', 'Daily'),
        ('weekly', 'Weekly'),
        ('monthly', 'Monthly')
    ]

    """

    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('done', 'Done'),
    ]

    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]


    RECURRING_CHOICES = [
        ('none', 'None'),
        ('daily', 'Daily'),
        ('weekly', 'Weekly'),
        ('monthly', 'Monthly')
    ]


    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tasks")
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='pending')
    priority = models.CharField(max_length=15, choices=PRIORITY_CHOICES, default='medium')
    recurrence = models.CharField(max_length=15, choices=RECURRING_CHOICES, default='none')
    recurrence_end = models.DateTimeField(null=True, blank=True) #specify when the task should stop recurring
    due_date = models.DateTimeField(null=True, blank=True)
    tags = models.ManyToManyField(Tag, related_name="tags", blank=True)
    start_time = models.TimeField(null=True, blank=True)
    end_time = models.TimeField(null=True, blank=True)
    time_spent= models.DurationField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


    def is_overdue(self):
        """Check if the task is overdue."""
        return self.due_date < timezone.now() and self.status != 'done'

