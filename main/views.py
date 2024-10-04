from django.shortcuts import render

# Create your views here.

from main.models import Project,Skill,Qualification

def index_view(request):
    return render(request, 'index.html',
                  {
                      'projects':Project.objects.all(),
                      'skills':Skill.objects.all(),
                      'qualification':Qualification.objects.all()
                      
                      })