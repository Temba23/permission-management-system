from django.db import models
from authentication.models import CustomUser

# Create your models here.
class Data(models.Model):
    user = models.ForeignKey(CustomUser, related_name="user_data", on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=50)
    context = models.CharField(max_length=25)
