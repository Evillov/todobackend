from django.shortcuts import render

# Create your views here.
from rest_framework import generics, permissions
from .serializers import TodoSerializer 
from todo.models import Todo

class TodoList(generics.ListAPIView):
# ListAPIView требует два обязательных атрибута, serializer_class и queryset.
# Мы указываем TodoSerializer, который мы реализовали ранее 
      serializer_class = TodoSerializer
      def get_queryset(self):
            user = self.request.user
            return Todo.objects.filter(user=user).order_by('-created')
      
class TodoListCreate(generics.ListCreateAPIView):
      serializer_class = TodoSerializer
      permission_classes = [permissions.IsAuthenticated] # - устанавливает возможность доступа к этому API только авторизованным пользователям
      
      def get_queryset(self):
            user = self.request.user            
            return Todo.objects.filter(user=user).order_by('-created')
      
      def perform_create(self, serializer):
            serializer.save(user=self.request.user)

