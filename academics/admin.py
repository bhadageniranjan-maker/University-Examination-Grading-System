from django.contrib import admin
from .models import Department, Semester, Professor, Subject


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ("name", "code")
    search_fields = ("name", "code")


@admin.register(Semester)
class SemesterAdmin(admin.ModelAdmin):
    list_display = ("department", "number", "academic_year")
    list_filter = ("department", "academic_year")


@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
    list_display = ("name", "employee_id", "email", "department")
    list_filter = ("department",)
    search_fields = ("name", "employee_id", "email")


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ("code", "name", "semester", "credits")
    list_filter = ("semester",)
    search_fields = ("code", "name")

# Register your models here.
