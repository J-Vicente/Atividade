from django.shortcuts import render
from django.http import HttpResponse
from .models import Curso
from django.shortcuts import get_object_or_404

# Create your views here.

def index(request):
    curso = Curso.objects.all()
    context = {'curso': curso}
    return render(request,"index.html",context)

def curso(request,id):
    curso = get_object_or_404(Curso, id=id)
    context = {'curso': curso}
    return render(request,"curso.html",context)