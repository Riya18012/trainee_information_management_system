from django import forms
from .models import Course, Trainee, Trainer, TrainingCenter, Enrollment, Certificate

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'

class TraineeForm(forms.ModelForm):
    class Meta:
        model = Trainee
        fields = '__all__'

class TrainerForm(forms.ModelForm):
    class Meta:
        model = Trainer
        fields = '__all__'

class TrainingCenterForm(forms.ModelForm):
    class Meta:
        model = TrainingCenter
        fields = '__all__'

class EnrollmentForm(forms.ModelForm):
    class Meta:
        model = Enrollment
        fields = '__all__'

class CertificateForm(forms.ModelForm):
    class Meta:
        model = Certificate
        fields = '__all__'
