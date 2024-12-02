
from django.contrib import admin
from django.urls import path
from xenofobia import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),  
    path('main/', views.main_view, name='main'),
    path('thank-you/', views.thank_you_view, name='thank_you_view'),
    path('', views.inicial_view, name='inicial'),  # 登录页面
    path('register/', views.register_view, name='register'),  # 注册页面
    path('salir/', views.salir_view, name='salir'),
    
]


# 添加静态文件支持
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)



   
