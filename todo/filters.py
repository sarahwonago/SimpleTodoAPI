from django_filters import rest_framework as filters
from .models import Task

class TaskFilter(filters.FilterSet):
    """
    FilterSet for filtering tasks by status and tags.
    """

    # Filter by tag (ManyToMany field), looking for tasks that have a specific tag.
    tags = filters.CharFilter(field_name="tags__name", lookup_expr="icontains")

    # Filter by status (pending, in_progress, done)
    status = filters.ChoiceFilter(choices=Task.STATUS_CHOICES)

    class Meta:
        model = Task
        fields = ['tags', 'status', 'priority']
