from django.db import models


# Create your models here.

class Todo(models.Model):
    """任务清单"""
    todo = models.CharField('任务清单', max_length=240)

    class Meta:
        db_table = 'tb_todo'
        verbose_name = '任务'
