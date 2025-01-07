from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import TodoItem, TodoList
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    todo_lists = TodoList.objects.all()
    context = {"todo_lists": todo_lists}
    return render(request, "todos/index.html", context)

def list(request, todo_list_id):
    this_list = get_object_or_404(TodoList, pk=todo_list_id)
    context = {"todo_list": this_list}
    return render(request, "todos/list.html", context)


def item(request, item_id):
    this_item = get_object_or_404(TodoItem, pk=item_id)
    context = { "item": this_item}
    return render(request, "todos/item.html", context)