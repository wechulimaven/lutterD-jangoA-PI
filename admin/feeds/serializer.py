from .models import VideoInfo, FeedPosts, userPaidVideo

from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from django.contrib.auth.models import User


class VideoInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = VideoInfo
        fields = ('videoUrl', 'thumbUrl', 'coverUrl', 'aspectRatio')


class FeedPostsSerializer(serializers.ModelSerializer):

    class Meta:
        model = FeedPosts
        fields = ('id', 'userName', 'postContent', 'feedUploaderId',
         'postId', 'postLikeCount', 'userThumbnail', 'postImage',
         'mediaType', 'isPayable', 'amount', 'video', 'userContacts',
         'email', 'postalCode', 'shop', 'shopLocation', 'shopUrl',
         'address', 'birthday')

class PaidUserVidSerializer(serializers.ModelSerializer):

    class Meta:
        model = userPaidVideo
        fields = ('post', 'payerId', 'checkoutRequestID', 'paymentConfirmed')

class UserSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password',
        )
        validators = [
            UniqueTogetherValidator(
                queryset=User.objects.all(),
                fields=['username', 'email']
            )
        ]

