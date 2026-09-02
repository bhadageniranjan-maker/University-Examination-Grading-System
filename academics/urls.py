from django.urls import path
from django.contrib.auth import views as auth_views

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
    # USER LOGIN
    # =====================================================

    path(
        "login/",
        auth_views.LoginView.as_view(
            template_name="academics/login.html"
        ),
        name="login"
    ),


    # =====================================================
    # USER LOGOUT
    # =====================================================

    path(
        "logout/",
        auth_views.LogoutView.as_view(),
        name="logout"
    ),


    # =====================================================
    # DEPARTMENTS
    # =====================================================

    path(
        "departments/",
        views.departments,
        name="departments"
    ),

    path(
        "departments/add/",
        views.department_create,
        name="department_create"
    ),

    path(
        "departments/<int:pk>/edit/",
        views.department_edit,
        name="department_edit"
    ),

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


    # =====================================================
    # VERSION 2
    # ROOMS
    # =====================================================

    path(
        "rooms/",
        views.rooms,
        name="rooms"
    ),


    # =====================================================
# VERSION 2
# EXAMS
# =====================================================

path(
    "exams/",
    views.exams,
    name="exams"
),

path(
    "exams/add/",
    views.exam_create,
    name="exam_create"
),

path(
    "exams/timetable/",
    views.exam_timetable,
    name="exam_timetable"
),

path(
    "exams/<int:pk>/edit/",
    views.exam_edit,
    name="exam_edit"
),

path(
    "exams/<int:pk>/delete/",
    views.exam_delete,
    name="exam_delete"
),
]