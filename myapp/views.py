from django.forms import model_to_dict
from django.shortcuts import redirect, render
from django.http import HttpResponse, JsonResponse
from django.urls import reverse
from .models import Project, Task
from django.shortcuts import get_object_or_404

#
# PROJECT
#
def getAllProjects(request):
    allProjects = list(Project.objects.all().values())
    return render(request, "index.html", {
        "projects": allProjects
    })

def project(request, id):
    project = Project.objects.get(id = id) 
    allProjectTasks = _getAllTaskByProjectId(id) 
    return render(request, "singleProject.html", {
        "project": project,
        "tasks": allProjectTasks
    })

def createProject(request):
    name = request.POST["name"]
    Project.objects.create(name=name)
    return redirect(reverse("home"))


#
# TASK
#
def createTask(request, id):
    title = request.POST["title"]
    description = request.POST["description"]
    Task.objects.create(title=title, description=description, project_id=id)
    return redirect(reverse("oneProject", kwargs={"id": id}))

def _getAllTaskByProjectId(id):
    task = list(Task.objects.filter(project = id))
    return task

def getTaskInfoById(request, id):
    task = Task.objects.get(id = id)
    return JsonResponse(model_to_dict(task), safe=False)

def deleteTask(request, idTask):
    task = Task.objects.get(id = idTask) 
    task.delete()
    return HttpResponse("OK", status=200)

def doneTask(request, idTask):
    task = Task.objects.get(id = idTask) 
    task.done = True
    task.save()
    return HttpResponse("OK", status=200)