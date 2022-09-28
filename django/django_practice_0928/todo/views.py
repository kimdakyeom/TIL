from django.shortcuts import render, redirect
from .models import Todo


def index(request):
    todos = Todo.objects.order_by("id")
    context = {
        "todos": todos,
    }

    return render(request, "todo/index.html", context)


def create(request):
    content = request.GET.get("content")
    priority = request.GET.get("priority")
    deadline = request.GET.get("deadline")
    Todo.objects.create(
        content=content,
        priority=priority,
        deadline=deadline,
    )

    return redirect("todo:index")


def modify(request, pk):
    todo = Todo.objects.get(pk=pk)
    if todo.completed == False:
        todo.completed = True
    else:
        todo.completed = False

    todo.save()
    return redirect("todo:index")


def delete(request, pk):
    todo = Todo.objects.get(pk=pk)
    todo.delete()

    return redirect("todo:index")
