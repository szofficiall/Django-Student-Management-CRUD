from django.shortcuts import render, redirect, get_object_or_404
from .models import StudentData
from .forms import StudentForm

# Create your views here.


# Create Student
def create_students(request):

    form = StudentForm()

    if request.method == "POST":
        form = StudentForm(request.POST)

        if form.is_valid():
            form.save()
            return render(request, "student_success_msg.html")
    return render(request, "student_form.html", {"form": form})


# Read Students
def read_students(request):
    students = StudentData.objects.all()
    return render(request, "student_list.html", {"students": students})


def student_details(request, pk):
    students = get_object_or_404(StudentData, pk=pk)
    return render(request, "student_details.html", {"students": students})


def update_students(request, pk):
    student = get_object_or_404(StudentData, pk=pk)

    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)

        if form.is_valid():
            form.save()
            return redirect("studentform:read_students")
    else:
        form = StudentForm(instance=student)
        return render(request, "student_form.html", {"form": form })


def student_delete(request, pk):
    student = get_object_or_404(StudentData, pk=pk)

    if not student:
        return redirect("studentform:read_students")

    if request.method == "POST":
        student.delete()
        return redirect("studentform:read_students")
    else:
        return render(request, "student_confrim_delete.html")
