from django.db import models

from users.models import User


class Customer(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    middle_name = models.CharField(max_length=20)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    passport_number = models.CharField(max_length=14)  # Example: 12345678-12345
    disability = models.BooleanField(default=False)
    created_by = models.ForeignKey(to=User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - created by {self.created_by.email}"
