from django.shortcuts import render,redirect
from .models import TodoList
from .forms import TodoListForm

def home(request):
    task = TodoList.objects.all()
    context = {
        'tasks':task
    }
    return render(request, 'todoapp/home.html', context)


def add_task(request):
    if request.method == "POST":
        form = TodoListForm(request.POST)
        if form.is_valid():
            form.save()
            task = form.cleaned_data.get('task')
            return redirect('home-page')
    else:
        form = TodoListForm()
    return render(request, 'todoapp/add.html', {'form':form})

def delete_task(request, pk):  #To delete completed tasks
    if request.method == "POST":
        delete_todo = TodoList.objects.get(id=pk)
        delete_todo.delete()
        return redirect('home-page')