from django import forms

from .models import (
    Department,
    Semester,
    Subject,
    Professor,
    Exam
)


# =========================================================
# DEPARTMENT FORM
# =========================================================

class DepartmentForm(forms.ModelForm):

    class Meta:

        model = Department

        fields = [
            "name",
            "code",
            "description"
        ]

        widgets = {

            "name": forms.TextInput(
                attrs={
                    "placeholder": "Enter department name"
                }
            ),

            "code": forms.TextInput(
                attrs={
                    "placeholder": "Enter department code"
                }
            ),

            "description": forms.Textarea(
                attrs={
                    "placeholder": "Enter department description",
                    "rows": 4
                }
            ),
        }


# =========================================================
# SEMESTER FORM
# =========================================================

class SemesterForm(forms.ModelForm):

    class Meta:

        model = Semester

        fields = [
            "department",
            "number",
            "academic_year"
        ]


# =========================================================
# SUBJECT FORM
# =========================================================

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


# =========================================================
# PROFESSOR FORM
# =========================================================

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


# =========================================================
# EXAM FORM
# VERSION 2
# =========================================================

class ExamForm(forms.ModelForm):

    class Meta:

        model = Exam

        fields = [
            "subject",
            "room",
            "exam_date",
            "start_time",
            "end_time",
            "student_count"
        ]

        widgets = {

            "exam_date": forms.DateInput(
                attrs={
                    "type": "date"
                }
            ),

            "start_time": forms.TimeInput(
                attrs={
                    "type": "time"
                }
            ),

            "end_time": forms.TimeInput(
                attrs={
                    "type": "time"
                }
            ),

            "student_count": forms.NumberInput(
                attrs={
                    "min": "1",
                    "placeholder": "Enter number of students"
                }
            ),
        }


    # =====================================================
    # VALIDATION
    # =====================================================

    def clean(self):

        cleaned_data = super().clean()

        subject = cleaned_data.get("subject")
        room = cleaned_data.get("room")
        exam_date = cleaned_data.get("exam_date")
        start_time = cleaned_data.get("start_time")
        end_time = cleaned_data.get("end_time")
        student_count = cleaned_data.get("student_count")


        # =================================================
        # 1. CHECK START AND END TIME
        # =================================================

        if start_time and end_time:

            if end_time <= start_time:

                raise forms.ValidationError(
                    "End time must be later than start time."
                )


        # =================================================
        # 2. CHECK ROOM CAPACITY
        # =================================================

        if room and student_count:

            if student_count > room.capacity:

                raise forms.ValidationError(
                    f"Student count ({student_count}) "
                    f"exceeds the room capacity "
                    f"({room.capacity})."
                )


        # =================================================
        # 3. CHECK ROOM TIME CONFLICT
        # =================================================

        if (
            room
            and exam_date
            and start_time
            and end_time
        ):

            conflicting_exams = Exam.objects.filter(
                room=room,
                exam_date=exam_date
            ).exclude(
                pk=self.instance.pk
            )


            for existing_exam in conflicting_exams:

                if (
                    start_time < existing_exam.end_time
                    and
                    end_time > existing_exam.start_time
                ):

                    raise forms.ValidationError(
                        "This room is already occupied "
                        "by another examination during "
                        "the selected time."
                    )


        # =================================================
        # 4. CHECK SAME SUBJECT DUPLICATE
        # =================================================

        if (
            subject
            and exam_date
        ):

            duplicate_exam = Exam.objects.filter(
                subject=subject,
                exam_date=exam_date
            ).exclude(
                pk=self.instance.pk
            ).exists()


            if duplicate_exam:

                raise forms.ValidationError(
                    "This subject already has an "
                    "examination scheduled on this date."
                )


        return cleaned_data