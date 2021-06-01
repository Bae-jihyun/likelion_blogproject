# from blogproject.blog.views import login
from django.contrib import admin
from login import views
from django.urls import path
from . import views

urlpatterns = [
    # path('admin/',admin.site.urls),
    # path('',views.login,name = "login"),
    path('signup/',views.signup, name = "signup"),
    # path('login/',views.login, name = "login"),
    path('logout/',views.logout,name ="logout"),
]
