from django.urls import path
from .views import TaskListView, TaskDetailsView

urlpatterns = [
    # path('auth/', ),  # user auth
    path('task/details/<int:pk>/', TaskDetailsView.as_view()),  # create/view/edit task
    path('task/details/all/', TaskListView.as_view()),  # view all user tasks
    # path('logs/', ),
]
