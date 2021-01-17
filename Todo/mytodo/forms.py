from django import forms


# 借助forms实现任务提交功能
class TodoForm(forms.Form):
    todo = forms.CharField(label='任务', error_messages={
        'required':'请填写任务内容！',
        'max_length':'任务内容过长。'
    })
