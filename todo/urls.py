from django.urls import path
from .views import TaskListCreateView, TaskDetailView

urlpatterns = [
    path("", TaskListCreateView.as_view(), name="tasks"),
    path("<uuid:pk>/", TaskDetailView.as_view(), name="task-detail"),
]
