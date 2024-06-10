from django.urls import path
from .views import DataView, ChangeRole, GivePermission

urlpatterns = [
    path('data/', DataView.as_view(), name="register"),
    path('data/<int:pk>/', DataView.as_view(), name="register"),
    path('role-change/', ChangeRole.as_view(), name="change_role"),
    path('give-permission/', GivePermission.as_view(), name="give_user_permission")
]