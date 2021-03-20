from django.db import models

class VideoInfo(models.Model):
    videoUrl = models.CharField(max_length=50)
    thumbUrl = models.CharField(max_length=50)
    coverUrl = models.CharField(max_length=50)
    aspectRatio = models.DecimalField(max_digits=5, decimal_places=4)   


    def __str__(self):
        return f'{self.videoUrl}'

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'VideoInfo'
        verbose_name_plural = 'VideoInfo'

class FeedPosts(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    userName = models.CharField(max_length=50)
    postContent = models.TextField()
    feedUploaderId = models.CharField(max_length=50)
    postId = models.CharField(max_length=50)
    postLikeCount = models.IntegerField()
    userThumbnail = models.CharField(max_length=50)
    postImage = models.CharField(max_length=50)
    mediaType = models.BooleanField(default = False)
    isPayable = models.BooleanField(default = False)
    amount = models.CharField(max_length=50)
    video = models.ForeignKey(VideoInfo, on_delete=models.CASCADE)

    userContacts = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    postalCode = models.CharField(max_length=50)
    shop = models.CharField(max_length=50)
    shopLocation = models.CharField(max_length=50)
    shopUrl = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    birthday = models.CharField(max_length=50)
    def __str__(self):
        return f'{self.userName}, {self.userContacts}'

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'FeedPosts'
        verbose_name_plural = 'FeedPosts'

class userPaidVideo(models.Model):
    post = models.ForeignKey(FeedPosts, on_delete=models.CASCADE)
    payerId = models.CharField(max_length=50)
    checkoutRequestID = models.CharField(max_length=50)
    paymenConfirmed = models.BooleanField()
    # mediaType = models.BooleanField(default = False)


    def __str__(self):
        return f'{self.post}, {self.payerId}'

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'userPaidVideo'
        verbose_name_plural = 'userPaidVideos'

