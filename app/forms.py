from django import forms
from app.models import Student



class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields='__all__'
    botcatcher=forms.CharField(max_length=10,required=False,widget=forms.HiddenInput())

    