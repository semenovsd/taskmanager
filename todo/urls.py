from django.urls import path
from .views import TaskListView, TaskDetailsView, TaskLogsView, TaskFilterView

urlpatterns = [
    path('task/<int:pk>/', TaskDetailsView.as_view()),  # create/view/edit task
    path('task/all/', TaskListView.as_view()),  # view all user tasks
    path('task/filter/<str:filter>', TaskFilterView.as_view()),  # view tasks with filter
    path('task/logs/<int:pk>/', TaskLogsView.as_view()),  # view tasks logs
]
