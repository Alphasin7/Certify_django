from django.shortcuts import render

# Create your views here.
# certification/views.py
from django.shortcuts import render
from .utils import check_eligibility
from students.models import Student

def certification_status(request, student_id):
    student = Student.objects.get(id=student_id)
    eligible, reason = check_eligibility(student)
    return render(request, 'certification/status.html', {
        'student': student,
        'eligible': eligible,
        'reason': reason,
    })
