from django import forms
from .models import School

class SchoolForm(forms.ModelForm):
    class Meta:
        model = School
        # fields = "__all__"
        # fields = ["questions_name"]
        exclude = ["created_time"]
        