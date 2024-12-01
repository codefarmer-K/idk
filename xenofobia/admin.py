from django.contrib import admin
from .models import UserMessage
from .models import CustomUser

admin.site.register(UserMessage)
admin.site.register(CustomUser)
