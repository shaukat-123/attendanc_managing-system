# models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    is_manager = models.BooleanField(default=False)

# Add related_name arguments to avoid clash with auth.User
CustomUser.groups.field.remote_field.related_name = 'customuser_groups'
CustomUser.user_permissions.field.remote_field.related_name = 'customuser_permissions'



class Staff(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    working_days = models.CharField(max_length=7)  # eg. '1111100' for Mon-Fri
    shifts = models.CharField(max_length=100)  # eg. '9:00 AM - 5:00 PM, 1:00 PM - 9:00 PM'


class Attendance(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='attendance_images/')
