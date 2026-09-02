from django.shortcuts import (
    render,
    redirect,
    get_object_or_404
)

from django.contrib.auth.decorators import login_required

from .models import (
    Department,
    Semester,
    Subject,
    Professor,
    Room,
    Exam
)

from .forms import (
    DepartmentForm,
    SemesterForm,
    SubjectForm,
    ProfessorForm,
    ExamForm
)


# =========================================================
# DASHBOARD
# =========================================================

@login_required
def home(request):

    context = {
        "department_count": Department.objects.count(),
        "semester_count": Semester.objects.count(),
        "subject_count": Subject.objects.count(),
        "professor_count": Professor.objects.count(),
        "room_count": Room.objects.count(),
        "exam_count": Exam.objects.count(),
    }

    return render(
        request,
        "academics/home.html",
        context
    )


# =========================================================
# DEPARTMENTS - VIEW ALL
# =========================================================

@login_required
def departments(request):

    departments = Department.objects.all().order_by("name")

    return render(
        request,
        "academics/departments.html",
        {
            "departments": departments
        }
    )


# =========================================================
# SEMESTERS - VIEW ALL
# =========================================================

@login_required
def semesters(request):

    semesters = Semester.objects.select_related(
        "department"
    ).order_by(
        "department",
        "number"
    )

    return render(
        request,
        "academics/semesters.html",
        {
            "semesters": semesters
        }
    )


# =========================================================
# SUBJECTS - VIEW ALL
# =========================================================

@login_required
def subjects(request):

    subjects = Subject.objects.select_related(
        "semester",
        "semester__department"
    ).prefetch_related(
        "professors"
    ).order_by(
        "semester",
        "name"
    )

    return render(
        request,
        "academics/subjects.html",
        {
            "subjects": subjects
        }
    )


# =========================================================
# PROFESSORS - VIEW ALL
# =========================================================

@login_required
def professors(request):

    professors = Professor.objects.select_related(
        "department"
    ).prefetch_related(
        "subjects"
    ).order_by("name")

    return render(
        request,
        "academics/professors.html",
        {
            "professors": professors
        }
    )


# =========================================================
# VERSION 2
# ROOMS - VIEW ALL
# =========================================================

@login_required
def rooms(request):

    rooms = Room.objects.all().order_by(
        "building",
        "room_number"
    )

    total_capacity = sum(
        room.capacity
        for room in rooms
    )

    return render(
        request,
        "academics/rooms.html",
        {
            "rooms": rooms,
            "total_capacity": total_capacity
        }
    )


# =========================================================
# VERSION 2
# EXAMS - VIEW ALL
# =========================================================

@login_required
def exams(request):

    exams = Exam.objects.select_related(
        "subject",
        "room"
    ).order_by(
        "exam_date",
        "start_time"
    )

    return render(
        request,
        "academics/exams.html",
        {
            "exams": exams
        }
    )


# =========================================================
# VERSION 2
# EXAMINATION TIMETABLE
# =========================================================

@login_required
def exam_timetable(request):

    exams = Exam.objects.select_related(
        "subject",
        "room"
    ).order_by(
        "exam_date",
        "start_time"
    )

    return render(
        request,
        "academics/exam_timetable.html",
        {
            "exams": exams
        }
    )


# =========================================================
# VERSION 2
# EXAM - CREATE
# =========================================================

@login_required
def exam_create(request):

    if request.method == "POST":

        form = ExamForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect("exams")

    else:

        form = ExamForm()

    return render(
        request,
        "academics/exam_form.html",
        {
            "form": form,
            "page_title": "Add Examination",
            "page_description": "Create a new university examination schedule"
        }
    )


# =========================================================
# VERSION 2
# EXAM - EDIT
# =========================================================

@login_required
def exam_edit(request, pk):

    exam = get_object_or_404(
        Exam,
        pk=pk
    )

    if request.method == "POST":

        form = ExamForm(
            request.POST,
            instance=exam
        )

        if form.is_valid():

            form.save()

            return redirect("exams")

    else:

        form = ExamForm(
            instance=exam
        )

    return render(
        request,
        "academics/exam_form.html",
        {
            "form": form,
            "page_title": "Edit Examination",
            "page_description": "Update examination schedule details"
        }
    )


# =========================================================
# VERSION 2
# EXAM - DELETE
# =========================================================

@login_required
def exam_delete(request, pk):

    exam = get_object_or_404(
        Exam,
        pk=pk
    )

    if request.method == "POST":

        exam.delete()

        return redirect("exams")

    return render(
        request,
        "academics/confirm_delete.html",
        {
            "object": exam,
            "object_type": "Examination"
        }
    )


# =========================================================
# DEPARTMENT - CREATE
# =========================================================

@login_required
def department_create(request):

    if request.method == "POST":

        form = DepartmentForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect("departments")

    else:

        form = DepartmentForm()

    return render(
        request,
        "academics/department_form.html",
        {
            "form": form,
            "page_title": "Add Department"
        }
    )


# =========================================================
# DEPARTMENT - EDIT
# =========================================================

@login_required
def department_edit(request, pk):

    department = get_object_or_404(
        Department,
        pk=pk
    )

    if request.method == "POST":

        form = DepartmentForm(
            request.POST,
            instance=department
        )

        if form.is_valid():

            form.save()

            return redirect("departments")

    else:

        form = DepartmentForm(
            instance=department
        )

    return render(
        request,
        "academics/department_form.html",
        {
            "form": form,
            "page_title": "Edit Department"
        }
    )


# =========================================================
# DEPARTMENT - DELETE
# =========================================================

@login_required
def department_delete(request, pk):

    department = get_object_or_404(
        Department,
        pk=pk
    )

    if request.method == "POST":

        department.delete()

        return redirect("departments")

    return render(
        request,
        "academics/confirm_delete.html",
        {
            "object": department,
            "object_type": "Department"
        }
    )