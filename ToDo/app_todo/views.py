from django.db import IntegrityError
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from .forms import ToDoForm
from .models import ToDoModel
from django.utils import timezone
from django.contrib.auth.decorators import login_required


def home_view(request):
    return render(request, 'todo/home.html')


def signup_view(request):
    if request.method == 'GET':
        context = {
            'form': UserCreationForm(),
        }
        return render(request, 'todo/signup.html', context)
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('list_todo')
            except IntegrityError:
                context = {
                    'form': UserCreationForm(),
                    'error': 'That username has already been taken. Please choose a new username',
                }
                return render(request, 'todo/signup.html', context)
        else:
            context = {
                'form': UserCreationForm(),
                'error': "Passwords didn't match",
            }
            return render(request, 'todo/signup.html', context)

@login_required
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')


def login_view(request):
    if request.method == 'GET':
        context = {
            'form': AuthenticationForm(),
        }
        return render(request, 'todo/login.html', context)
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            context = {
                'form': AuthenticationForm(),
                'error': "Username or password didn't match",
            }
            return render(request, 'todo/login.html', context)
        else:
            login(request, user)
            return redirect('list_todo')

@login_required
def list_todo_view(request):
    todos = ToDoModel.objects.filter(user=request.user, date_completed__isnull=True)
    context = {
        'todos': todos,
    }
    return render(request, 'todo/list_todo.html', context)

@login_required
def create_todo_view(request):
    if request.method == 'GET':
        context = {
            'form': ToDoForm(),
        }
        return render(request, 'todo/create_todo.html', context)
    else:
        try:
            form = ToDoForm(request.POST)
            new_todo = form.save(commit=False)
            new_todo.user = request.user
            new_todo.save()
            return redirect('list_todo')
        except ValueError:
            context = {
                'form': ToDoForm(),
                'error': 'Bad data passed in. Try again.',
            }
            return render(request, 'todo/create_todo.html', context)

@login_required
def todo_view(request, todo_pk):
    todo = get_object_or_404(ToDoModel, pk=todo_pk, user=request.user)
    context = {
        'todo': todo,
    }
    return render(request, 'todo/todo.html', context)

@login_required
def todo_change_view(request, todo_pk):
    todo = get_object_or_404(ToDoModel, pk=todo_pk, user=request.user)
    if request.method == 'GET':
        form = ToDoForm(instance=todo)
        context = {
            'change_todo': todo,
            'form': form,
        }
        return render(request, 'todo/change_todo.html', context)
    else:
        try:
            form = ToDoForm(request.POST, instance=todo)
            form.save()
            return redirect('todo', todo_pk=todo_pk)
        except ValueError:
            context = {
                'change_todo': todo,
                'form': form,
                'error': 'Bad data passed in. Try again.',
            }
            return render(request, 'todo/change_todo.html', context)

@login_required
def todo_complete_view(request, todo_pk):
    todo = get_object_or_404(ToDoModel, pk=todo_pk, user=request.user)
    if request.method == 'POST':
        todo.date_completed = timezone.now()
        todo.save()
        return redirect('list_todo')

@login_required
def todo_delete_view(request, todo_pk):
    todo = get_object_or_404(ToDoModel, pk=todo_pk, user=request.user)
    if request.method == 'POST':
        todo.delete()
        return redirect('list_todo')

@login_required
def list_todo_complete_view(request):
    todos = ToDoModel.objects.filter(user=request.user, date_completed__isnull=False)
    context = {
        'todos': todos,
    }
    return render(request, 'todo/list_todo_complete.html', context)
@login_required
def todo_complete_info_view(request, todo_pk):
    todo = get_object_or_404(ToDoModel, pk=todo_pk, user=request.user)
    context = {
        'todo': todo,
    }
    return render(request, 'todo/todo_complete.html', context)
