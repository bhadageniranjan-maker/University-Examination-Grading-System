from django.shortcuts import (
    render,
    redirect,
    get_object_or_404
)

from .models import (
    Department,
    Semester,
    Subject,
    Professor
)

from .forms import (
    DepartmentForm,
    SemesterForm,
    SubjectForm,
    ProfessorForm
)


# =========================================================
# DASHBOARD
# =========================================================

def home(request):

    context = {
        "department_count": Department.objects.count(),
        "semester_count": Semester.objects.count(),
        "subject_count": Subject.objects.count(),
        "professor_count": Professor.objects.count(),
    }

    return render(
        request,
        "academics/home.html",
        context
    )


# =========================================================
# DEPARTMENTS - VIEW ALL
# =========================================================

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
# DEPARTMENT - CREATE
# =========================================================

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