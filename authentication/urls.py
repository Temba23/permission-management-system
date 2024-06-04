from django.urls import path
from .views import RegisterUserAPIView, LoginAPIView, LogoutAPIView

urlpatterns = [
    path('register/', RegisterUserAPIView.as_view(), name="register"),
    path('login/', LoginAPIView.as_view(), name="register"),
    path('logout/', LogoutAPIView.as_view(), name="register"),
]