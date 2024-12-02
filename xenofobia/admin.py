from django.contrib import admin
from .models import UserMessage
from .models import CustomUser
from .models import Video

class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'uploaded_at')  # 显示标题和上传时间
    search_fields = ('title',)  # 可通过标题搜索


admin.site.register(UserMessage)
admin.site.register(CustomUser)
admin.site.register(Video, VideoAdmin)
