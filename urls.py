"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from xenofobia import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', views.register, name='register'),
    path('about_us/', views.about_us, name='about_us'),
    path('video/', views.video, name='video'),  # 添加视频播放页面
    path('', views.about_us, name='home'),  # 这里是新增的行，将空路径重定向到 'about' 页面
    path('tabbed/', views.tabbed_page, name='tabbed_page'),
]
