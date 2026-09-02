from django.contrib import admin

from .models import (
    Department,
    Semester,
    Professor,
    Subject,
    Room,
    Exam
)


# =========================================================
# DEPARTMENT
# =========================================================

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "code",
    )

    search_fields = (
        "name",
        "code",
    )


# =========================================================
# SEMESTER
# =========================================================

@admin.register(Semester)
class SemesterAdmin(admin.ModelAdmin):

    list_display = (
        "department",
        "number",
        "academic_year",
    )

    list_filter = (
        "department",
        "academic_year",
    )


# =========================================================
# PROFESSOR
# =========================================================

@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "employee_id",
        "email",
        "department",
    )

    search_fields = (
        "name",
        "employee_id",
        "email",
    )


# =========================================================
# SUBJECT
# =========================================================

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):

    list_display = (
        "code",
        "name",
        "semester",
        "credits",
    )

    search_fields = (
        "code",
        "name",
    )

    list_filter = (
        "semester",
    )


# =========================================================
# ROOM
# VERSION 2
# =========================================================

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):

    list_display = (
        "room_number",
        "building",
        "capacity",
    )

    search_fields = (
        "room_number",
        "building",
    )


# =========================================================
# EXAM
# VERSION 2
# =========================================================

@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):

    list_display = (
        "subject",
        "room",
        "exam_date",
        "start_time",
        "end_time",
        "student_count",
    )

    list_filter = (
        "exam_date",
        "room",
        "subject",
    )

    search_fields = (
        "subject__name",
        "subject__code",
        "room__room_number",
    )