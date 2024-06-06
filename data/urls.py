from django.urls import path
from .views import DataView

urlpatterns = [
    path('data/', DataView.as_view(), name="register"),
    path('data/<int:pk>/', DataView.as_view(), name="register"),
]