from django.shortcuts import redirect, render,get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth
from .models import Blog
from django.utils import timezone

def home(request):
    blogs=Blog.objects  #Query set (여러개)
    return render(request, 'home.html', {'blogs':blogs})

def detail(request,blog_id):
    details=get_object_or_404(Blog, pk=blog_id) #id값을 갖는 Blog 클래스를 가져오거나 못가져오면 404 에러를 나타내라 (쿼리셋이아닌 객체 한개)
    return render(request,'detail.html',{'detail':details})

def myself(request):
    return render(request, 'myself.html')

def intro(request):
    return render(request,'intro.html')

def new(request):
    return render(request, 'new.html')

def create(request):
    blog=Blog()
    blog.title=request.POST.get('title',False)
    blog.body=request.POST.get('body',False)
    blog.pub_date=timezone.datetime.now()
    blog.save()
    return redirect('/blog/'+str(blog.id))

# def signup(request):
#     if request.method=="POST":
#         if request.POST['password1'] == request.POST['password2']:
#             user =User.object.create_user(username=request.POST["username"],password = request.POST['password1'])
#             auth.login(request,user)
#             return redirect('home')
#     return render(request,'signup.html')

# def login(request):
#     if request.method=="POST":
#         username = request.POST['username']
#         password = request.POST['password']
#         user = auth.authenticate(request, username = username,password=password)
#         if user is not None :
#             auth.login(request,user)
#             return redirect('home')
#         else:
#             return render(request,'login.html',{'error':"아이디나 비밀번호가 잘못되었습니다."})
#     return render(request,'login.html')

# def logout(request):
#     if request.method=="POST":
#         auth.logout(request)
#         redirect('home')
#     return render(request,'login.html')