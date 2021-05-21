from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from board import models
from .models import Board,Topic,Post
from django.http import Http404
from django.contrib.auth.models import User
from .forms import NewTopicForm , NewPostForm ,UserForm
from django.utils import timezone
from datetime import date
# Create your views here.
def home(request):
     if request.session.get('is_login',None):
        boards = models.Board.objects.all()
        request.session.set_expiry(0)   #设置关闭浏览器时清空session
        return render(request,'board/home.html',{'boards':boards})
     else:
         return redirect('login')
def login(request):
    if request.session.get('is_login',None):
        return redirect('home')
    if request.method == 'POST':

        login_form = UserForm(request.POST)
        print(login_form)
        if  login_form.is_valid():
            print('d')
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            print(username,password)
            #检查用户是否存在
            try:
                user = User.objects.get(username=username)
                print(user.username,user.password)
            except:
                message='用户不存在'
                return render(request,'board/login.html',locals() )
            if user.password == password:
                request.session['is_login'] = True
                request.session['user_id'] = user.id
                request.session['user_name'] = user.username
                request.session.set_expiry(0)    #设置关闭浏览器后清空session
                return redirect('home')
            else:
                message='密码不正确!'
                return render(request,'board/login.html',locals())
        else:
            message = '请检查输入的格式是否正确！！！'
            return render(request,'board/login.html',locals())
    login_form = UserForm()
    return render(request,'board/login.html',locals())
#展示版面和主题
def board_topics(request,pk):
    try:
        board = Board.objects.get(pk = pk)
    except Board.DoesNotExist:
        raise Http404
    return render(request,'board/topics.html',{'board':board}) #

#展示某个主题的回复内容(pk为板块的id,pk1为主题的id)
def board_topic_posts(request,pk,pk1):
    try:
        topic = Topic.objects.get(pk = pk1)
        board = Board.objects.get(pk = pk)
    except  Topic.DoesNotExist:
        raise  Http404
    return  render(request,'board/posts.html',{'topic':topic,'board':board})

#为某个板块创建一个新主题(pk为板块的id)
def new_topic(request,pk):
    board = get_object_or_404(Board,pk=pk)
    user = User.objects.first() #获取当前登录用户
    if  request.method == 'POST':
        form = NewTopicForm(request.POST) #form是包含topic类的一个实例
        if form.is_valid():
            subject = form.cleaned_data.get('subject')
            topic = form.save(commit=False)
            topic.subject = subject
            topic.board = board
            topic.starter = user

            topic.save()
            #创建一个回复贴
            post = Post.objects.create(
                message = form.cleaned_data.get('message'),
                topic = topic,
                created_by = user
            )
            return redirect('board_topics',pk = board.id)
    else:
        form = NewTopicForm()
    return render(request,'board/new_topic.html',{'board':board,'form':form})
#为某个主题(topic)创建新的回复(pk为topic的id)
def new_post(request,pk,pk1):
    topic = get_object_or_404(Topic,pk = pk1)#获取当前主题信息
    board = get_object_or_404(Board,pk = pk )#获取当前板块信息
    user = User.objects.first()
    if request.method == 'POST':
        form = NewPostForm(request.POST) #form是包含post类的一个实例。
        if form.is_valid():
            print('valid')
            message = form.cleaned_data.get('message')
            post = form.save(commit=False)
            post.topic_id = pk1
            post.message = message
            post.created_by = user
            post.created_at = timezone.now().strftime("%Y-%m-%d %H:%M:%S")
            post.save()

            return redirect('board_tpoic_posts',pk = pk, pk1=pk1) #返回当前主题

    else:
        form = NewPostForm()
    return render(request,'board/new_post.html',{'topic':topic,'form':form,'board':board})

#删除主题
def del_topic(request,pk):
    return

#删除回复贴
def del_post(request,pk,pk1):
    return