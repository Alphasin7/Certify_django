# certification/utils.py
from students.models import Student
from scores.models import Score
from subjects.models import Subject

def check_eligibility(student):
    # Simple logic: check if all required scores are above a threshold
    required_subjects = Subject.objects.all()  # Define required subjects for certification
    for subject in required_subjects:
        try:
            score = Score.objects.get(student=student, subject=subject)
            if score.score < 70:  # Arbitrary threshold
                return False, "Insufficient score in a required subject"
        except Score.DoesNotExist:
            return False, "Missing required subject scores"
    return True, "Eligible for certification"
