from django.contrib import admin

from gesperson.forms import *
from .models import *

# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    form = StudentForm

class TeacherAdmin(admin.ModelAdmin):
    form = TeacherForm


admin.site.register(Student, StudentAdmin)
admin.site.register(Teacher, TeacherAdmin)