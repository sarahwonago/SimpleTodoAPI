
from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

urlpatterns = [
    path("admin/", admin.site.urls),

    # djoser urls for user management
    path("api/auth/", include('djoser.urls')),

    # djoser urls for JWT token endpoints
    path("api/auth/", include('djoser.urls.jwt')),

    # API Documentation
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/schema/redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
    path("api/schema/swagger/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger"),

    # Task Management
    path("api/task/", include('todo.urls')),
]
