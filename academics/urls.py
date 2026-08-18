from django.urls import path

from . import views


urlpatterns = [

    # =====================================================
    # DASHBOARD
    # =====================================================

    path(
        "",
        views.home,
        name="home"
    ),


    # =====================================================
    # DEPARTMENTS
    # =====================================================

    # View all departments
    path(
        "departments/",
        views.departments,
        name="departments"
    ),

    # Add department
    path(
        "departments/add/",
        views.department_create,
        name="department_create"
    ),

    # Edit department
    path(
        "departments/<int:pk>/edit/",
        views.department_edit,
        name="department_edit"
    ),

    # Delete department
    path(
        "departments/<int:pk>/delete/",
        views.department_delete,
        name="department_delete"
    ),


    # =====================================================
    # SEMESTERS
    # =====================================================

    path(
        "semesters/",
        views.semesters,
        name="semesters"
    ),


    # =====================================================
    # SUBJECTS
    # =====================================================

    path(
        "subjects/",
        views.subjects,
        name="subjects"
    ),


    # =====================================================
    # PROFESSORS
    # =====================================================

    path(
        "professors/",
        views.professors,
        name="professors"
    ),

]