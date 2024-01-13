from django import forms
from .models import *
from django.forms import ModelForm

#création du formulaire student 
class StudentForm(ModelForm):

    class Meta:
        model = Student
        #fields =["first_name","last_name", "birth_date","tel","email", "speciality"] 
        fields = '__all__'

    def clean_nom(self):
        nom = self.cleaned_data.get['first_name']
        if any(char.isdigit() for char in nom):
            raise forms.ValidationError("Le champs nom ne doit pas contenir les caratères numériques.")
        return nom
    clean_nom
    def clean_prenom(self):
        prenom=self.cleaned_data.get['last_name']
        if any(char.isdigit() for char in prenom):
            raise forms.ValidationError('Le champs prenom ne doit pas contenir les caractères numériques.')
        return prenom
    clean_prenom



#creation du formulaire teachers

class TeacherForm(ModelForm):
    class Meta:
        model = Teacher
        #fields = ["first_name", "last_name","birth_date", "tel", "email", "pathway"]
        fields = '__all__'

    def clean_nom(self):
        nom = self.cleaned_data.get('first_name')
        if any(char.isdigit() for char in nom):
            raise forms.ValidationError("Le champs nom ne doit pas contenir les caratères numériques.")
        return nom
    clean_nom
    def clean_prenom(self):
        prenom=self.cleaned_data.get('last_name')
        if any(char.isdigit() for char in prenom):
            raise forms.ValidationError('Le champs prenom ne doit pas contenir les caractères numériques.')
        return prenom
    clean_prenom


