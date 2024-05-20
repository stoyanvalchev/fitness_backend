from django.urls import path
from . import views

urlpatterns = [
    path("users/", views.Users.as_view(), name="users-view"),
    path("users/<int:pk>/", views.UserUpdateDestroy.as_view(), name='user-update')
]