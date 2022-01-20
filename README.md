# Author: Arysbay Dastan. Group: SE-2004
# ToDo app with authentication in Django!
Task is to build a ToDo application with authentication using Django Web Framework 

# Installation

```bash
pip install Django
```

```bash
pip install migrate
```

Install pgAdmin
Install for both desktop and web modes:
```bash
sudo apt install pgadmin4
```
Install for desktop mode only:
```bash
sudo apt install pgadmin4-desktop
```
Install for web mode only: 
```bash
sudo apt install pgadmin4-web 
```
Configure the webserver, if you installed pgadmin4-web:
```bash
sudo /usr/pgadmin4/bin/setup-web.sh
```

# Usage

```bash
python3.8 manage.py runserver

Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
January 20, 2022 - 08:17:06
Django version 4.0.1, using settings 'TodoProject.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

# Examples

```python
urlpatterns = [
    path('login/', CustomLoginView.as_view(), name= 'login'),
    path('logout/', LogoutView.as_view(next_page ='login'), name= 'logout'),
    path('register/', RegisterPage.as_view(), name= 'register'),
    path('list/', views.list_todo_items, name= 'tasks'),
    path('insert_todo', views.insert_todo_item, name='insert_todo_item'),
    path('delete_todo/<int:todo_id>/', views.delete_todo_item, name='delete_todo_item')
]
```

```python
class CustomLoginView(LoginView):
    template_name = 'todos/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('tasks')
```



![Screenshot 2022-01-20 at 2 21 32 PM](https://user-images.githubusercontent.com/74294979/150300447-cdec11fd-52f1-4f5f-9e10-552a0130906f.png)




