from django.urls import path

from . import views

app_name = "todos"
urlpatterns = [
    path("", views.index, name="index"),
    path("list/<int:todo_list_id>/", views.list, name="list"),
    path("item/<int:item_id>/", views.item, name="item")
]
