from django.http import HttpResponse
from django.shortcuts import render
from django_redis import get_redis_connection
import json


# Create your views here.


def VueTodo(request):
    redis_conn = get_redis_connection('todo')
    # if request.method == 'GET':
    #     result = redis_conn.get('todos')
    #     print(result)
    #
    #     return render(request, 'vuetodo.html')

    if request.method == 'POST':
        req_data = json.loads(request.body)

        key = 'todos'
        value = req_data[key]
        print(value)
        result = redis_conn.set(key, value)

        print(result)
    return render(request, 'vuetodo.html')