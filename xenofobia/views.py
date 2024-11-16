# xenofobia/views.py
from django.shortcuts import render, redirect
from .forms import RegistrationForm

# 用户注册视图
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()  # 保存用户数据
            return redirect('login')  # 注册成功后跳转到登录页面（需要创建登录页面）
    else:
        form = RegistrationForm()
    return render(request, 'xenofobia/register.html', {'form': form})

# 团队介绍视图
def about_us(request):
    return render(request, 'xenofobia/about_us.html')

# 视频播放视图
def video(request):
    return render(request, 'xenofobia/videos.html')
def tabbed_page(request):
    return render(request, 'xenofobia/tabbed_page.html')