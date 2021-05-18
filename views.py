from django.shortcuts import render, redirect
from .models import Tarea
from .forms import TareaForm

# Create your views here.

def index(request):
    tareas = Tarea.objects.all()
    context = {
        'tareas': tareas
    }
    return render(request, 'todo/home.html', context)


def agregar(request):
    """Add a new topic."""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = TareaForm()
    else:
        # POST data submitted; process data.
        form = TareaForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo_app:index')

    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'todo/agregar.html', context)

def eliminar(request, tarea_id):
    tarea = Tarea.objects.get(id=tarea_id)
    tarea.delete()
    return redirect('todo_app:index')


def editar(request, tarea_id):
    """Edit an existing entry."""
    tarea = Tarea.objects.get(id=tarea_id)
    if request.method != 'POST':
        # Initial request; pre-fill form with the current entry.
        form = TareaForm(instance=tarea)
    else:
        # POST data submitted; process data.
        form = TareaForm(instance=tarea, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo_app:index')

    context = {'tarea': tarea, 'form': form}
    return render(request, 'todo/editar.html', context)
