from django.shortcuts import render
from mytodo.models import Todo
from mytodo.forms import TodoForm


# Create your views here.


def TodoList(request):
    # 需求:点击输入框，将任务写入数据库

    todolist = Todo.objects.all().order_by('-id')
    for todo in todolist:
        print(todo.todo)

    if request.method == 'GET':
        # GET请求获取所有已有任务
        form = TodoForm()

    else:
        # POST请求提交任务
        form = TodoForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Todo.objects.create(todo=data.get('todo'))

    todo_data = {
        'todolist': todolist,
        'form': form
    }

    return render(request, 'todolist.html', todo_data)
