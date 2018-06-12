#coding:utf-8

from django.shortcuts import render,redirect
from django.db.models import Q
import hashlib
from models import *


def register(request):
    return  render(request,'df_user/register.html')

def register_handle(request):
    name = request.POST.get('user_name')
    pwd = request.POST.get('pwd')
    cpwd = request.POST.get('cpwd')
    email = request.POST.get('email')


    if pwd!=cpwd:
        return redirect('/user/register')

    s1 = hashlib.sha1()
    s1.update(pwd)
    upwd = s1.hexdigest()

    user=UserInfo()
    user.uname=name
    user.upwd=upwd
    user.uemail=email
     #user.save()
    #zhu ce oK zhuan dao denglu

    return redirect('/user/login/')


def login(request):
    return render(request,'df_user/login.html')


def login_handle(request):
    name = request.POST.get('username')
    pwd = request.POST.get('pwd')

    s1 = hashlib.sha1()
    s1.update(pwd)
    upwd = s1.hexdigest()

    q1 =Q(uname__contains=name)
    q2 = Q(upwd__contains=upwd)
    list =UserInfo.objects.filter(q1 & q2)
    if list:
        username =list[0].uname
        request.session['name']=username
        return redirect('/df_goods/index/')
    else:
        return redirect('/user/login/')


def user_center_info(request):
    return render(request,'df_user/user_center_info.html')





















