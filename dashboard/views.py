# dashboard/views.py
from django.shortcuts import render, get_object_or_404
from students.models import Student
from scores.models import Score
from certification.models import Certification

def dashboard_overview(request):
    """
    Displays an overview of all students, showing their names, majors, and certification status.
    """
    students = Student.objects.all()
    certifications = Certification.objects.all()
    
    # Pass a dictionary with each student's certification status for easier access in the template
    certification_statuses = {cert.student.id: cert.is_certified for cert in certifications}

    context = {
        'students': students,
        'certification_statuses': certification_statuses,
    }
    return render(request, 'dashboard/overview.html', context)


def student_detail(request, student_id):
    """
    Displays detailed information about a specific student, including their scores and certification status.
    """
    student = get_object_or_404(Student, id=student_id)
    scores = Score.objects.filter(student=student)
    certification = Certification.objects.filter(student=student).first()  # Assume one certification per student

    context = {
        'student': student,
        'scores': scores,
        'certification': certification,
    }
    return render(request, 'dashboard/student_detail.html', context)


def certified_students(request):
    """
    Displays a list of all certified students.
    """
    certified_students = Student.objects.filter(certification__is_certified=True)

    context = {
        'certified_students': certified_students,
    }
    return render(request, 'dashboard/certified_students.html', context)


def non_certified_students(request):
    """
    Displays a list of all students who are not yet certified.
    """
    non_certified_students = Student.objects.filter(certification__is_certified=False)

    context = {
        'non_certified_students': non_certified_students,
    }
    return render(request, 'dashboard/non_certified_students.html', context)
