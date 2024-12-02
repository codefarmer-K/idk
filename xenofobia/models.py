# Create my models .
from django.db import models

class UserMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"
class CustomUser(models.Model):
    name = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)  # 明文加密将在视图中处理

    def __str__(self):
        return self.name
class Video(models.Model):
    title = models.CharField(max_length=255)  # 视频标题
    description = models.TextField(blank=True, null=True)  # 视频描述
    video_file = models.FileField(upload_to='videos/')  # 视频文件路径
    uploaded_at = models.DateTimeField(auto_now_add=True)  # 上传时间

    def __str__(self):
        return self.title
