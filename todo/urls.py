from django.urls import path
from .views import TaskListCreateView, TaskDetailView, TagViewSet

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("tags", TagViewSet)

urlpatterns = [
    path("", TaskListCreateView.as_view(), name="tasks"),
    path("<uuid:pk>/", TaskDetailView.as_view(), name="task-detail"),
]

urlpatterns += router.urls