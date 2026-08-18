from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name} ({self.code})"


class Semester(models.Model):
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        related_name="semesters"
    )
    number = models.PositiveIntegerField()
    academic_year = models.CharField(max_length=20)

    class Meta:
        unique_together = ("department", "number", "academic_year")

    def __str__(self):
        return f"{self.department.code} - Semester {self.number}"


class Professor(models.Model):
    name = models.CharField(max_length=100)
    employee_id = models.CharField(max_length=30, unique=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, blank=True)

    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        related_name="professors"
    )

    def __str__(self):
        return self.name


class Subject(models.Model):
    semester = models.ForeignKey(
        Semester,
        on_delete=models.CASCADE,
        related_name="subjects"
    )
    name = models.CharField(max_length=150)
    code = models.CharField(max_length=30, unique=True)
    credits = models.PositiveIntegerField()

    professors = models.ManyToManyField(
        Professor,
        related_name="subjects",
        blank=True
    )

    def __str__(self):
        return f"{self.code} - {self.name}"

# Create your models here.
