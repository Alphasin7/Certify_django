from django.db import models

# Create your models here.
# subjects/models.py
from django.db import models

class Subject(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10, unique=True)
    credits = models.IntegerField()
    
    def __str__(self):
        return self.name
