from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from .models import Todo
from django.contrib.auth.views import LoginView
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.views import View
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

# Create your views here.
def list_todo_items(request):

    context = {'todo_list' : Todo.objects.all() }



    return render(request, 'todos/todo_list.html', context)

def insert_todo_item(request:HttpRequest):
    todo = Todo(content=request.POST['content'])
    todo.save()
    return redirect('/todos/list/')

def delete_todo_item(request, todo_id):
    todo_to_delete = Todo.objects.get(id=todo_id)
    todo_to_delete.delete()
    return redirect('/todos/list')
    
class CustomLoginView(LoginView):

    template_name = 'todos/login.html'
    fields = '__all__'
    redirect_authenticated_user = True  

    # success_url = reverse_lazy
    def get_success_url(self):
        return reverse_lazy('tasks')



class RegisterPage(FormView):
    template_name = 'todos/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True 
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('tasks')
        return super(RegisterPage, self).get(*args, **kwargs)