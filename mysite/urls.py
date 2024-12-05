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
    path('enviroment/', views.enviroment_view, name='enviroment'),
    path('add_comment/<int:post_id>/', views.add_comment, name='add_comment'),
    path('delete_post/<int:post_id>/', views.delete_post, name='delete_post'),
    path('delete_comment/<int:comment_id>/', views.delete_comment, name='delete_comment'),
]



# 添加静态文件支持
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

