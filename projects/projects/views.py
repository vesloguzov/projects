from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.core.context_processors import csrf
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import UpdateView, DeleteView

from .models import Project

from .form import Project_form


#def projects(request):
 #   return HttpResponse('Привет!')

def projects(request):
    projects = Project.objects.all()
    args = {}
    args['projects'] = projects
    args['title'] = 'Проекты'
    return render(request,'index.html', args)

@login_required()
def new_project(request):
    if request.method == 'POST':
        form = Project_form(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            comment = form.cleaned_data['comment']
            project = Project(name=name, comment=comment)
            project.save()
            return redirect('/')
    args = {}
    args.update(csrf(request))
    args['form'] = Project_form()
    return render(request,'new_project.html', args)

@login_required()
def project(request, pk):
    try:
        project = Project.objects.get(id=pk)
    except ObjectDoesNotExist:
         return HttpResponse(status=404)
    return render(request, 'project.html', {'project':project})

class ProjectDelete(DeleteView):
    model = Project
    fields = []
    success_url = '/'

class ProjectUpdate(UpdateView):
    model = Project
    fields = ['name', 'comment']
    success_url = '/'