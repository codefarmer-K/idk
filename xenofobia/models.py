# Create my models .
from django.db import models
from django.utils import timezone
from django.utils import timezone
from django.contrib.auth import get_user_model

# 获取自定义用户模型
CustomUser = get_user_model()


class UserMessage(models.Model):
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # 将时间转换为本地时区（智利时间）
        local_time = timezone.localtime(self.submitted_at)
        return f"{local_time}"

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
    likes_count = models.PositiveIntegerField(default=0)  # 点赞总数

    def __str__(self):
        return self.title


class Like(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)  # 点赞的用户
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name='likes')  # 点赞的视频
    created_at = models.DateTimeField(auto_now_add=True)  # 点赞时间

    class Meta:
        unique_together = ('user', 'video')  # 每个用户对每个视频只能点赞一次




class Post(models.Model):
    # 发言内容
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)  # 发言的客户
    content = models.TextField()  # 发言内容

    def __str__(self):
        return f"Post by {self.user.username}"

class Comment(models.Model):
    # 评论内容
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)  # 评论对应的发言
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)  # 评论的客户
    content = models.TextField()  # 评论内容

    def __str__(self):
        return f"Comment by {self.user.username} on {self.post.id}"
