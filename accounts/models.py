from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

# Create your models here.
class CustomUserModel(AbstractUser):
    full_names = models.CharField(max_length=50)
    hostel_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=13)
    is_registered = models.BooleanField(default= False)

    def __str__(self):
        return self.username
    
#model to store registered details
class RegistrationDetails(models.Model):
    full_names = models.CharField(max_length=50)
    hostel_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=13)
    security_code = models.UUIDField(default=uuid.uuid4, editable=False)
    is_registered = models.BooleanField(default=False)

    def __str__(self):
        return self.full_names