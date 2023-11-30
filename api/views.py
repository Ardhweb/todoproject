from rest_framework import viewsets
from rest_framework.response import Response
from todoapp.models import Tag, TodoList
from api.serializers import TodoListSerializer
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404


class TodoViewSet(viewsets.ModelViewSet):
    queryset = TodoList.objects.all()
    serializer_class = TodoListSerializer
    #@action(detail=True, methods=['get'],url_path='item')
    # def get_queryset(self):
    #     queryset = TodoList.objects.all()
    #     return queryset

    def perform_create(self, serializer):
        serializer.save()






