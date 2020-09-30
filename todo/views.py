from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser


from rest_framework import generics
from .serializer import TaskDetailSerializer


# Create your views here.
# @csrf_exempt
class TaskCreateView(generics.CreateAPIView):
    serializer_class = TaskDetailSerializer
