from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import SchoolForm
# Create your views here.

def index(request):
    if request.POST:
        questionform = SchoolForm(request.POST)
        if questionform.is_valid():
            questionform.save()
    
    
    questions = School.objects.all()
    
    context = {
        "questions": questions
    }
    
    return render(request, 'index.html', context)

def Menu(request, question_id):
    if request.POST:
        son = request.POST["ovoz"]
        savol = menus.objects.get(id=son)
        savol.ovozlar_soni += 1
        savol.save()
        
    savollar = menus.objects.filter(school_id=question_id)
    questions = School.objects.get(id=question_id)
    context = {
        "savollar": savollar,
        "questions": questions
    }
    
    return render(request, 'savol.html', context)



def add_question(request):
    form = SchoolForm()
    
    ctx = {
        "form": form,
    }
    
    return render(request, 'add_question.html', ctx)