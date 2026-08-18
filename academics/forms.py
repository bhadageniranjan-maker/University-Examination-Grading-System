from django import forms

from .models import (
    Department,
    Semester,
    Professor,
    Subject
)


class DepartmentForm(forms.ModelForm):

    class Meta:
        model = Department

        fields = [
            "name",
            "code",
            "description"
        ]


class SemesterForm(forms.ModelForm):

    class Meta:
        model = Semester

        fields = [
            "department",
            "number",
            "academic_year"
        ]


class ProfessorForm(forms.ModelForm):

    class Meta:
        model = Professor

        fields = [
            "name",
            "employee_id",
            "email",
            "phone",
            "department"
        ]


class SubjectForm(forms.ModelForm):

    class Meta:
        model = Subject

        fields = [
            "semester",
            "name",
            "code",
            "credits",
            "professors"
        ]