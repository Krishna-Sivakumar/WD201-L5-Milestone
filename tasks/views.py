# Add all your views here
from django.http import HttpResponseRedirect
from django.views.generic import View
from django.views.generic.edit import CreateView, DeleteView
from django.views.generic.list import ListView

from tasks.models import Task


class CurrentTasksView(CreateView):
    template_name = "current.html"
    context_object_name = "tasks"

    model = Task
    fields = ["title", "priority"]
    success_url = "/tasks"

    def get_context_data(self, **kwargs):
        context = {
            "tasks": Task.objects.filter(completed=False, deleted=False).order_by("priority")
        }
        return super().get_context_data(**context)

    def form_valid(self, form):
        incoming_priority = form.cleaned_data["priority"]

        if Task.objects.filter(priority=incoming_priority).count() > 0:
            current_tasks = Task.objects.filter(
                priority__gte=incoming_priority,
                completed=False,
                deleted=False
            ).order_by("priority")
            counter = incoming_priority

            for task in current_tasks:
                if counter != task.priority:
                    break
                task.priority += 1
                task.save()
                counter += 1

        self.object = form.save()
        return HttpResponseRedirect(self.success_url)


class CompletedView(ListView):
    template_name = "completed.html"
    context_object_name = "tasks"

    def get_queryset(self):
        return Task.objects.filter(completed=True)


class TaskDeleteView(DeleteView):
    model = Task
    template_name = "delete_confirmation.html"
    success_url = "/tasks"


class CompleteTaskView(View):
    def get(self, request, pk):
        Task.objects.filter(id=pk).update(completed=True)
        return HttpResponseRedirect("/tasks/")


class AllTasksView(ListView):
    template_name = "all.html"
    context_object_name = "tasks"

    def get_queryset(self):
        return {
            "current": Task.objects.filter(completed=False, deleted=False),
            "completed": Task.objects.filter(completed=True)
        }
