from django.shortcuts import render
from django.shortcuts import redirect, render,get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth
# Create your views here.
# def signup(request):
#     return render(request,'signup.html')

# def login(request):
#     return render(request,'login.html')


def signup(request):
    if request.method=="POST":
        if request.POST['password1'] == request.POST['password2']:
            user =User.object.create_user(username=request.POST["username"],password = request.POST['password1'])
            auth.login(request,user)
            return redirect('home')
    return render(request,'signup.html')

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

def logout(request):
    if request.method=="POST":
        auth.logout(request)
        redirect('home')
    return render(request,'login.html')