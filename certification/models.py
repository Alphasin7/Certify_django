from django.db import models

# Create your models here.
# certification/models.py
from django.db import models
from students.models import Student

class Certification(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    certification_date = models.DateField(auto_now_add=True)
    is_certified = models.BooleanField(default=False)
    certification_reason = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.student.name} - Certified: {self.is_certified}"
