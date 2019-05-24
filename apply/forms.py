from django import forms
from .models import apply

class ApplyForm(forms.ModelForm):
    class Meta:
        model = apply
        fields = ['name', 'major', 'student_id', 'email', 'phone', 'body', 'file']
