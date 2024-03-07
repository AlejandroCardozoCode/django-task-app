from django.urls import path
from . import views

urlpatterns = [
    #
    # Projects
    #
    path('', views.getAllProjects, name="home"),
    path('projects/<int:id>', views.project, name="oneProject"),
    path('create_project', views.createProject, name= "create_project"),
    #
    # Tasks
    #
    path('tasks/', views._getAllTaskByProjectId),
    path('task/<int:id>', views.getTaskInfoById),
    path('projects/<int:id>/create_task', views.createTask, name= "create_task"),
    path('delete_task/<int:idTask>', views.deleteTask, name= "delete_task"),
    path('done_task/<int:idTask>', views.doneTask, name= "done_task"),
]
