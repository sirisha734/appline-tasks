from django.db import models
from datetime import date

# Create your models here.
class Tasks(models.Model):
    task_name = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    assigned_date = models.DateField(default=date.today)
    due_date = models.DateField(default=date.today)
    priority_level = models.CharField(max_length=10)