from django.db import models
from django.contrib.auth.models import User
from mptt.models import MPTTModel, TreeForeignKey
import datetime
from django.utils import timezone

# Create your models here.

class TodoList(models.Model):
    title = models.CharField(max_length=100)
    created_date = models.DateTimeField("date created", default=timezone.now)
    created_by = models.ForeignKey(User, related_name='created_lists', on_delete=models.CASCADE)
    owned_by = models.ForeignKey(User, related_name='owned_lists', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class TodoItem(MPTTModel):
    task = models.CharField(max_length=200)
    created_date = models.DateTimeField("date created", default=timezone.now)
    due_date = models.DateTimeField("due date", null=True, blank=True)
    completed = models.BooleanField()
    completed_date = models.DateTimeField("date completed", null=True, blank=True)
    created_by = models.ForeignKey(User, related_name='created_items', on_delete=models.CASCADE)
    owned_by = models.ForeignKey(User, related_name='owned_items', on_delete=models.CASCADE)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='subtasks')
    parent_list = models.ForeignKey(TodoList, related_name="child_items", on_delete=models.CASCADE)

    def __str__(self):
        return self.task
    

class MPTTMeta:
    order_insertion_by = ['created_date']