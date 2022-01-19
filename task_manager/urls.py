from django.contrib import admin
from django.urls import path
import tasks.views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("tasks/", tasks.views.tasks_view),
    path("add-task/", tasks.views.add_task_view),
    path("delete-task/<int:task_index>/", tasks.views.delete_task_view),
    path("complete_task/<int:task_index>/", tasks.views.complete_task_view),
    path("completed_tasks/", tasks.views.completed_task_view),
    path("all_tasks/", tasks.views.all_tasks_view),
]
