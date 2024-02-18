from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Todo(models.Model):
      title = models.CharField(max_length=100)
      memo = models.TextField(blank=True)
      #Установить текущее время
      created = models.DateTimeField(auto_now_add =True)
      completed = models.BooleanField(default=False)
      #Пользователь, разместивший это
      user = models.ForeignKey(User,on_delete=models.CASCADE)
      def _str_(self):
            return self.title
      