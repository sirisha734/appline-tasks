from django.urls import path
from .views import TasksDetails, TasksInfo, TasksFetch, TasksFilter

urlpatterns = [
    path("tasks/", TasksDetails.as_view(), name="tasks"), # to get all tasks
    path("tasks/<int:id>/", TasksFetch.as_view(), name="tasksfetch"),
    path("tasks/<str:value>/", TasksInfo.as_view(), name="tasksinfo"),
    path("tasks/<str:parameter>/<str:value>/", TasksFilter.as_view(), name="taskfilter")
]