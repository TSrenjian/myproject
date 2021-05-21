from django.contrib import admin
from .models import Board
# Register your models here.
admin.site.register(Board)   #将Board模块注册，使得管理员能够管理Board