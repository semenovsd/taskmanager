from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser


from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from .permission import IsOwner
from .serializer import TaskViewSerializer, TaskDetailsSerializer
from .models import Task


# Create your views here.
# @csrf_exempt
class TaskDetailsView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskDetailsSerializer
    queryset = Task.objects.all()
    permission_classes = (IsAuthenticated, IsOwner, )


class TaskListView(generics.ListAPIView):
    serializer_class = TaskViewSerializer
    queryset = Task.objects.all()
    renderer_classes = (IsAuthenticated, IsAdminUser, )

