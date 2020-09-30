from django.views.decorators.csrf import csrf_exempt

from rest_framework import generics

from .permission import IsOwner
from .serializer import TaskViewSerializer, TaskDetailsSerializer, TaskLogsSerializer
from .models import Task


# Create your views here.
@csrf_exempt
class TaskDetailsView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskDetailsSerializer
    queryset = Task.objects.all()
    permission_classes = (IsOwner,)


class TaskListView(generics.ListAPIView):
    serializer_class = TaskViewSerializer
    permission_classes = (IsOwner,)


class TaskFilterView(generics.ListAPIView):
    serializer_class = TaskViewSerializer
    permission_classes = (IsOwner,)

    def get_queryset(self):
        """
        This view should return the tasks
        for the currently authenticated user.
        """
        task_filter = self.request.data.get('filter')
        return Task.objects.filter(filter=task_filter)


class TaskLogsView(generics.ListAPIView):
    serializer_class = TaskLogsSerializer
    permission_classes = (IsOwner,)
