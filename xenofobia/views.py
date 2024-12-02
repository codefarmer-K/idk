# xenofobia/views.py
from django.shortcuts import render, redirect
from .forms import RegistrationForm
from .forms import UserMessageForm# 替换为你的表单类路径
from django.contrib.auth import login, logout
from django.contrib import messages
from .models import CustomUser
from django.contrib.auth.hashers import make_password,check_password
from .models import Video

def main_view(request):
    user_name = request.session.get('user_name', None)
    if not user_name:
        return redirect('inicial')
    
    videos = Video.objects.all()  # 获取所有上传的视频
    return render(request, 'xenofobia/main.html', {'user_name': user_name, 'videos': videos})

def register_view(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        # 检查用户名和邮箱是否已存在
        if CustomUser.objects.filter(name=name).exists():
            messages.error(request, "User name ya existe ")
        elif CustomUser.objects.filter(email=email).exists():
            messages.error(request, "Correo ya existe")
        else:
            hashed_password = make_password(password)
            CustomUser.objects.create(name=name, email=email, password=hashed_password)
            messages.success(request, "Registro Existoso！")
            return redirect('inicial')  # 注册成功后重定向到登录页面

    return render(request, 'xenofobia/register.html')



def inicial_view(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = CustomUser.objects.get(email=email)
            if check_password(password, user.password):
                # 设置 session 存储用户信息
                request.session['user_id'] = user.id
                request.session['user_name'] = user.name

                # 显示欢迎消息
                messages.success(request, f"welcome back, {user.name}!")
                return redirect('main')  # 登录成功后跳转到 main 页面
            else:
                messages.error(request, "clave invalido")
        except CustomUser.DoesNotExist:
            messages.error(request, "usuario no existe, por favor registrate")

    return render(request, 'xenofobia/inicial.html')

# 感谢页面视图
def thank_you_view(request):
    return render(request, 'xenofobia/thank_you.html')




def salir_view(request):
    # 注销用户并清除会话中的用户名
    logout(request)
    request.session.flush()  # 清除会话
    return redirect('inicial')  # 重定向到登录页面


def main_view(request):
    user_name = request.session.get('user_name', None)
    if not user_name:
        return redirect('inicial')  # 未登录用户重定向到登录页面

    if request.method == 'POST':
        # 如果是表单提交请求
        form = UserMessageForm(request.POST)
        if form.is_valid():
            form.save()  # 保存表单数据到数据库
            return redirect('thank_you_view')  # 表单提交成功后跳转到感谢页面
    else:
        # 如果不是表单提交请求，渲染表单和视频列表
        form = UserMessageForm()
        videos = Video.objects.all()  # 获取所有视频

    return render(request, 'xenofobia/main.html', {
        'form': form,
        'user_name': user_name,
        'videos': videos,
    })
