from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from.models import Task
from.forms import TodoForm
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView

class Tasklistview(ListView):
    model=Task
    template_name = 'home.html'
    context_object_name = 'task1'
class TaskDetailview(DetailView):
    model=Task
    template_name = 'detail.html'
    context_object_name = 'task'

class TaskUpdateView(UpdateView):
    model=Task
    template_name = 'update.html'
    context_object_name = 'task'
    fields = ('Name','Priority','Date')

    def get_success_url(self):
        return reverse_lazy('cbvdetail',kwargs={'pk':self.object.id})

class TaskDeleteView(DeleteView):
    model=Task
    template_name = 'delete.html'
    success_url = reverse_lazy('cbvhome')


# Create your views here.
def Home (request):
    task1=Task.objects.all()
    if request.method=='POST':
        name=request.POST.get('Task','')
        priority=request.POST.get('Priority','')
        date=request.POST.get('Date','')
        task=Task(Name=name,Priority=priority,Date=date)
        task.save()
    return render(request,'home.html',{'task1':task1})
def Delete(request,taskid):
    task=Task.objects.get(id=taskid)
    if request.method == 'POST':
        task.delete()
        return redirect ('/')
    return render(request,'delete.html')

def Update (request,id):
    task=Task.objects.get(id=id)
    f=TodoForm (request.POST or None, instance=task)
    if f.is_valid():
        f.save()
        return redirect ('/')
    return render(request,'edit.html',{'f':f,'task':task})
