from django.shortcuts import render
from app.models import *
from app.forms import *
from django.http import HttpResponse
# Create your views here.

def create_student(request):
    ESFO=StudentForm()
    d={'ESFO':ESFO} 
    if request.method=='POST':
        SFDO=StudentForm(request.POST)
        if SFDO.is_valid():
            SFDO.save()
            return HttpResponse('student form is created')
        else:
            return HttpResponse('invalid data')
    return render(request,'create_student.html',d)
