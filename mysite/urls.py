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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.admin.views.decorators import staff_member_required



urlpatterns = [
    path('admin/logout/', views.custom_admin_logout, name='custom_admin_logout'),
    path('admin/', admin.site.urls),  
    path('main/', views.main_view, name='main'),
    path('thank-you/', views.thank_you_view, name='thank_you_view'),
    path('', views.inicial_view, name='inicial'),  # 登录页面
    path('register/', views.register_view, name='register'),  # 注册页面
    path('salir/', views.salir_view, name='salir'),
    path('contar/', views.contar_view, name='contar'),
]


# 添加静态文件支持
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)



   


   
