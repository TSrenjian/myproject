from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Board(models.Model):
    name = models.CharField(max_length=30,unique=True)
    description = models.CharField(max_length=256)
    def __str__(self):  #打印Board实例时将返回s实例的name属性
        return self.name

class Topic(models.Model):
    subject = models.CharField(max_length=128)
    last_update = models.DateTimeField(auto_now_add=True)
    board = models.ForeignKey(Board,related_name='topics',on_delete=models.CASCADE)
    #第二个参数on_delete表示级联删除，主表某个board删除了，从表中的数据也就删除了
    starter = models.ForeignKey(User,related_name='topics',on_delete=models.CASCADE)
    #related_name反向关联，指出创建者关联的是哪一个topic


class Post(models.Model):
    message = models.TextField(max_length=4000)
    topic = models.ForeignKey(Topic,related_name='posts',on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    created_by = models.ForeignKey(User,related_name='posts',on_delete=models.CASCADE,null=True)
    updated_by = models.ForeignKey(User,related_name='+',on_delete=models.CASCADE,null=True)
    #related_name='+'指示django不需要这种反向映射关系，可以忽略