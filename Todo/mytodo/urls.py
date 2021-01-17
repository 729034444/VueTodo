from django.urls import re_path
from mytodo import views

urlpatterns = [
    re_path(r'^$', views.TodoList, name='todolist'),
    # re_path(r'^/$', views.TodoList),
]
