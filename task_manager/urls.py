from django.contrib import admin
from django.urls import path
import tasks.views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("tasks/", tasks.views.CurrentTasksView.as_view()),
    path("delete-task/<int:pk>/", tasks.views.TaskDeleteView.as_view()),
    path("complete_task/<int:pk>/",
         tasks.views.CompleteTaskView.as_view()),
    path("completed_tasks/", tasks.views.CompletedView.as_view()),
    path("all_tasks/", tasks.views.AllTasksView.as_view()),
]
