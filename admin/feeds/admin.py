from django.contrib import admin
from .models import VideoInfo, FeedPosts, userPaidVideo

admin.site.register(VideoInfo)
admin.site.register(FeedPosts)
admin.site.register(userPaidVideo)
