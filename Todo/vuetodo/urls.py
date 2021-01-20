from django.urls import re_path
from vuetodo import views

url = 'http://localhost:63342/VueTodo/Todo/vuetodo/templates/vuetodo.html?_ijt=m39etgjiukjcrh0j0g0n11f25l#/all'
urlpatterns = [
    re_path(r'^$', views.VueTodo, name='vuetodo'),
    # re_path(r'^/$', views.TodoList),
]
