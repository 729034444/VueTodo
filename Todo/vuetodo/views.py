from django.shortcuts import render
from django_redis import get_redis_connection
import json

# Create your views here.


def VueTodo(request):
    redis_conn = get_redis_connection('todo')

    if request.method == 'GET':
        todolist = redis_conn.get('todolist')

    if request.method == 'POST':
        req_data = json.loads(request.body)
        changelist = redis_conn.set('todolist', todos)

