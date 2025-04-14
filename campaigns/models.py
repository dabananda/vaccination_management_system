from django.db import models
from users.models import User


class Campaign(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    vaccine_name = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='campaigns')

    def __str__(self):
        return self.title
