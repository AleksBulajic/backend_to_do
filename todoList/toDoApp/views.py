from rest_framework.generics import ListAPIView
from .models import ToDo
from .serializers import ToDoSerializer

class TaskListAPIView(ListAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer
