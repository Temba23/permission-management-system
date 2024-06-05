from django.urls import path
from .views import DataView

urlpatterns = [
    path('', DataView.as_view(), name="register"),
]