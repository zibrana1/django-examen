from . import views
from django.urls import path

#app_name = "gesperson"
urlpatterns =[
    path("", views.index),
    path("createTeacher/", views.add_teacher,name="createTeacher"),
    path("createStudent/", views.add_student, name="createStudent"),
    path("displayPerson/", views.display_person, name="displayPerson"),
    path("updateStudent/", views.update_student, name="update_student"),
]