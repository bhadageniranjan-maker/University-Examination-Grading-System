from django.db import models


# =========================================================
# DEPARTMENT
# =========================================================

class Department(models.Model):

    name = models.CharField(max_length=100)

    code = models.CharField(
        max_length=20,
        unique=True
    )

    description = models.TextField(
        blank=True
    )

    def __str__(self):
        return f"{self.name} ({self.code})"


# =========================================================
# SEMESTER
# =========================================================

class Semester(models.Model):

    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        related_name="semesters"
    )

    number = models.PositiveIntegerField()

    academic_year = models.CharField(
        max_length=20
    )

    class Meta:

        unique_together = (
            "department",
            "number",
            "academic_year"
        )

    def __str__(self):

        return f"{self.department.code} - Semester {self.number}"


# =========================================================
# PROFESSOR
# =========================================================

class Professor(models.Model):

    name = models.CharField(
        max_length=100
    )

    employee_id = models.CharField(
        max_length=30,
        unique=True
    )

    email = models.EmailField(
        unique=True
    )

    phone = models.CharField(
        max_length=15,
        blank=True
    )

    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        related_name="professors"
    )

    def __str__(self):

        return self.name


# =========================================================
# SUBJECT
# =========================================================

class Subject(models.Model):

    semester = models.ForeignKey(
        Semester,
        on_delete=models.CASCADE,
        related_name="subjects"
    )

    name = models.CharField(
        max_length=150
    )

    code = models.CharField(
        max_length=30,
        unique=True
    )

    credits = models.PositiveIntegerField()

    professors = models.ManyToManyField(
        Professor,
        related_name="subjects",
        blank=True
    )

    def __str__(self):

        return f"{self.code} - {self.name}"


# =========================================================
# ROOM
# VERSION 2
# =========================================================

class Room(models.Model):

    room_number = models.CharField(
        max_length=20,
        unique=True
    )

    building = models.CharField(
        max_length=100
    )

    capacity = models.PositiveIntegerField()

    def __str__(self):

        return f"{self.room_number} - {self.building}"


# =========================================================
# EXAM
# VERSION 2
# =========================================================

class Exam(models.Model):

    subject = models.ForeignKey(
        Subject,
        on_delete=models.CASCADE,
        related_name="exams"
    )

    room = models.ForeignKey(
        Room,
        on_delete=models.PROTECT,
        related_name="exams"
    )

    exam_date = models.DateField()

    start_time = models.TimeField()

    end_time = models.TimeField()

    student_count = models.PositiveIntegerField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):

        return (
            f"{self.subject.code} - "
            f"{self.exam_date} - "
            f"{self.room.room_number}"
        )