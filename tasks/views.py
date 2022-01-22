# Add all your views here
from django.http import HttpResponseRedirect
from django.shortcuts import render
from tasks.models import Task


def tasks_view(request):
    return render(request, "current.html", {"tasks": Task.objects.filter(completed=False, deleted=False)})


def add_task_view(request):
    task_value = request.GET.get("task")
    if task_value:
        Task(title=task_value).save()
    return HttpResponseRedirect("/tasks/")


def delete_task_view(request, task_index):
    Task.objects.filter(id=task_index).update(deleted=True)
    return HttpResponseRedirect("/tasks/")


def complete_task_view(request, task_index):
    Task.objects.filter(id=task_index).update(completed=True, deleted=False)
    return HttpResponseRedirect("/tasks/")


def completed_task_view(request):
    return render(request, "completed.html", {"tasks": Task.objects.filter(completed=True, deleted=False)})


def all_tasks_view(request):
    return render(
        request, "all.html", {"current": Task.objects.filter(completed=False, deleted=False),
                              "completed": Task.objects.filter(completed=True, deleted=False)}
    )
