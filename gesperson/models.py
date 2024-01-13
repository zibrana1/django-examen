from django.db import models

# Create your models here.

class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField()
    tel = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return "First Name :" +self.first_name +"  Last Name :" +self.last_name + " birth Date :" + str(self.birth_date) + " Telephone :" +str(self.tel) +"Email :"+ self.email

    class Meta:
        abstract = True

class Teacher(Person):
    speciality = models.CharField()

    def __str__(self):
        return super().__str__() + "speciality " + self.speciality 

class Student(Person):
    pathway = models.CharField()

    def __str__(self):
        return super().__str__() + "pathway " + self.pathway
