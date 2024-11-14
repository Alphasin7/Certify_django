from django.db import models

# Create your models here.
# students/models.py
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    major = models.CharField(max_length=100)  # Alternatively, create a Major model in a new app
    enrollment_date = models.DateField()
    
    def __str__(self):
        return self.name

