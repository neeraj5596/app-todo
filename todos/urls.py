from django.urls import path
from . import views

app_name = "todos"

urlpatterns = [
    path("", views.index, name="index"),
    path("add/", views.add_todo, name="add"),
    path("toggle/<int:pk>/", views.toggle_done, name="toggle"),
    path("delete/<int:pk>/", views.delete_todo, name="delete"),
]
