from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import Todo
from .forms import TodoForm


def index(request):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("todos:index")
    else:
        form = TodoForm()
    todos = Todo.objects.order_by("-created")
    return render(request, "todos/index.html", {"todos": todos, "form": form})


def toggle_done(request, pk):
    if request.method != "POST":
        return JsonResponse({"ok": False}, status=400)
    todo = get_object_or_404(Todo, pk=pk)
    todo.completed = not todo.completed
    todo.save()
    return JsonResponse({"ok": True, "completed": todo.completed})


def delete_todo(request, pk):
    if request.method != "POST":
        return JsonResponse({"ok": False}, status=400)
    todo = get_object_or_404(Todo, pk=pk)
    todo.delete()
    return JsonResponse({"ok": True})


def add_todo(request):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("todos:index")
    else:
        form = TodoForm()
    return render(request, "todos/add.html", {"form": form})
