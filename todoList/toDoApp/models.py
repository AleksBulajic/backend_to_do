from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ToDo(models.Model):
    task = models.CharField(max_length=100)
    created_on = models.DateTimeField(auto_now_add=True)
    added_by = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.task
    
    
    