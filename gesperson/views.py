from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from gesperson.forms import *

# Create your views here.

def index(request):
    return HttpResponse('Hello')

def add_teacher(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            teacher = form.save()
            teacher.save()
        return HttpResponse("Teacher not add")
    else:
        form = TeacherForm()
        return render(request, 'gesPersonnels/add_teacher.html', {"form":form})
    
def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save()
            student.save()
            return HttpResponse("Student succefully saved")
        return HttpResponse("Student not add")
    else:
        form = StudentForm()
        return render(request, "gesPersonnels/add_student.html", {"form": form})
    
def update_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    #object witch will be update
    students = Student.objects.filter(student=student)

    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save()
            student.update()
            return HttpResponse("student succesfull update")
        return HttpResponse("student does't update.")
    else:
        form = StudentForm()
        return render(request, "gesPersonnels/update_student.html", {"form": form, "students": students})



def display_person(request):
    students = Student.objects.all()
    teachers = Teacher.objects.all()

    return render(request, 'gesPersonnels/display_person.html', {'students':students, 'teachers': teachers})



