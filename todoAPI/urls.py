
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),

    # djoser urls for user management
    path("api/auth/", include('djoser.urls')),

    # djoser urls for JWT token endpoints
    path("api/auth/", include('djoser.urls.jwt')),
]
