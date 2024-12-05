# xenofobia/views.py
from sqlite3 import IntegrityError
from django.shortcuts import render, redirect
from .models import Video, Like
from .forms import RegistrationForm
from .forms import UserMessageForm# 替换为你的表单类路径
from django.contrib.auth import logout
from django.contrib import messages
from .models import CustomUser
from django.contrib.auth.hashers import make_password,check_password
from .models import Video
from django.contrib.auth import logout
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.db.models import F
from .models import Comment,Post
from .models import CustomUser
from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404

def delete_comment(request, comment_id):
    user_name = request.session.get('user_name', None)
    if not user_name:
        return redirect('inicial')  # 如果用户未登录，跳转到登录页面

    user = CustomUser.objects.get(name=user_name)
    comment = Comment.objects.get(id=comment_id)

    # 确保只有评论的作者可以删除评论
    if comment.user == user:
        comment.delete()

    return redirect('enviroment')  # 删除后返回论坛页面


# 删除帖子视图
def delete_post(request, post_id):
    user_name = request.session.get('user_name', None)
    if not user_name:
        return redirect('inicial')  # 如果用户未登录，跳转到登录页面

    user = CustomUser.objects.get(name=user_name)
    post = Post.objects.get(id=post_id)

    # 确保只有帖子作者可以删除帖子
    if post.user == user:
        post.delete()

    return redirect('enviroment')  # 删除后返回论坛页面


def add_comment(request, post_id):
    user_name = request.session.get('user_name', None)
    if not user_name:
        return redirect('inicial')  # 如果用户未登录，跳转到登录页面

    user = CustomUser.objects.get(name=user_name)
    post = Post.objects.get(id=post_id)

    if request.method == 'POST':
        comment_content = request.POST.get('comment_content')
        if comment_content:
            Comment.objects.create(post=post, user=user, content=comment_content)

    return redirect('enviroment')  # 提交评论后返回到论坛页面



def enviroment_view(request):
    user_name = request.session.get('user_name', None)
    if not user_name:
        return redirect('inicial')  # 如果用户未登录，跳转到登录页面

    user = CustomUser.objects.get(name=user_name)
    posts = Post.objects.all()  # 获取所有帖子

    if request.method == 'POST':
        content = request.POST.get('content')
        if content:
            # 保存新的发言
            Post.objects.create(user=user, content=content)

    return render(request, 'xenofobia/enviroment.html', {
        'user': user,  # 传递当前登录的用户
        'posts': posts,  # 传递所有的帖子
    })




@csrf_exempt  # 用于处理 POST 请求中的 CSRF 问题
def main_view(request):
    user_name = request.session.get('user_name', None)
    if not user_name:
        return redirect('inicial')

    user = CustomUser.objects.get(name=user_name)

    if request.method == 'POST':
        data = json.loads(request.body)  # 解析 JSON 数据
        video_id = data.get('video_id')
        action = data.get('action')  # 'like' or 'unlike'

        try:
            video = Video.objects.get(id=video_id)
            if action == 'like':
                # 添加点赞记录
                Like.objects.create(user=user, video=video)
                video.likes_count = F('likes_count') + 1
                video.save()
            elif action == 'unlike':
                # 移除点赞记录
                Like.objects.filter(user=user, video=video).delete()
                video.likes_count = F('likes_count') - 1
                video.save()
        except Video.DoesNotExist:
            return JsonResponse({'error': '视频不存在'}, status=404)
        except IntegrityError:
            return JsonResponse({'error': '重复点赞'}, status=400)

        return JsonResponse({'likes_count': video.likes_count})

    videos = Video.objects.all()
    for video in videos:
        video.liked_by_user = Like.objects.filter(user=user, video=video).exists()

    return render(request, 'xenofobia/main.html', {
        'user_name': user_name,
        'videos': videos,
    })


def custom_admin_logout(request):
    """自定义 admin logout 逻辑"""
    
    return redirect('main')  # 替换 'main' 为你的客户 main 页面名称





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
               
                return redirect('main')  # 登录成功后跳转到 main 页面
            else:
                messages.error(request, "clave invalido")
        except CustomUser.DoesNotExist:
            messages.error(request, "usuario no existe, por favor registrate")

    return render(request, 'xenofobia/inicial.html')

def contar_view(request):
    if request.method == 'POST':
        form = UserMessageForm(request.POST)
        if form.is_valid():
            form.save()  # 保存表单数据到数据库
            return redirect('thank_you_view')  # 跳转到感谢页面
    else:
        form = UserMessageForm()  # 显示空表单

    return render(request, 'xenofobia/contar.html', {'form': form})

# 感谢页面视图
def thank_you_view(request):
    return render(request, 'xenofobia/thank_you.html')






def salir_view(request):
    # 注销用户并清除会话中的用户名
    logout(request)
    request.session.flush()  # 清除会话
    return redirect('inicial')  # 重定向到登录页面
