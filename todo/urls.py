from django.urls import path
from .views import TaskCreateView

urlpatterns = [
    path('view/', TaskCreateView.as_view()),
    # path('auth/', ),
    # path('new_task/', ),
    # path('details/', ),
    # path('details/<int:pk>/', ),
    # path('logs/', ),
]
