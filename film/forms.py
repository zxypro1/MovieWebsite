from django.forms import forms,ModelForm
from .models import *

class Userform(ModelForm):
    class Meta:
        model = Consumer
        fields = ['username','password','email','age','gender','first_name','last_name','photo','nick_name','phone_num']

        labels = {
            'username':'用户名',
            'password':'密码',
            'email':'邮箱地址',
            'age':'年龄',
            'gender':'性别',
            'first_name':'第一名称',
            'last_name':'第二名称',
            'photo':"头像",
            'nick_name':'昵称',
            'phone_num':'电话号',
        }
