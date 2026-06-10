from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Todo, Comment
from .forms import TodoForm, CommentForm


def index(request):
    todos = Todo.objects.all()
    context = {
        'todos': todos
    }
    return render(request, 'todos/index.html', context)


def create(request):
    if request.method == 'POST':
        form = TodoForm(request.POST, request.FILES)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = request.user
            todo.save()
            return redirect('todos:index')
    else:
        form = TodoForm()
    context = {
        'form': form
    }
    return render(request, 'todos/create.html', context)


def detail(request, pk):
    todo = Todo.objects.get(pk=pk)
    context = {
        'todo': todo,
    }
    return render(request, 'todos/detail.html', context)


@login_required
def update(request, pk):
    todo = Todo.objects.get(pk=pk)
    if request.user != todo.user:
        return redirect('todos:detail', pk=pk)
    if request.method == 'POST':
        form = TodoForm(request.POST, request.FILES, instance=todo)
        if form.is_valid():
            todo = form.save()
            return redirect('todos:detail', pk=pk)
    else:
        form = TodoForm(instance=todo)
    context = {
        'form': form,
        'todo': todo
    }
    return render(request, 'todos/update.html', context)


def delete(request, pk):
    todo = Todo.objects.get(pk=pk)
    todo.delete()
    return redirect('todos:index')


@login_required
def comment_create(request, pk):
    todo = Todo.objects.get(pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.todo = todo
            comment.user = request.user
            comment.save()
    return redirect('todos:detail', pk=pk)


@login_required
def comment_delete(request, pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    if request.user == comment.user:
        comment.delete()
    return redirect('todos:detail', pk=pk)


@login_required
def toggle_complete(request, pk):
    todo = Todo.objects.get(pk=pk)
    todo.completed = not todo.completed
    todo.save()
    return redirect('todos:index')
