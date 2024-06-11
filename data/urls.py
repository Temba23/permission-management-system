from django.urls import path
from .views import DataView, ChangeRole, GivePermission, ConvertToQr

urlpatterns = [
    path('data/', DataView.as_view(), name="register"),
    path('data/<int:pk>/', DataView.as_view(), name="register"),
    path('role-change/', ChangeRole.as_view(), name="change_role"),
    path('give-permission/', GivePermission.as_view(), name="give_user_permission"),
    path('qr/', ConvertToQr.as_view(), name="qr_data"),

]