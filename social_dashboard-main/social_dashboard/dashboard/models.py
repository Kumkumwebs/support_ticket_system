from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(blank=True)
    #image = models.ImageField(upload_to='post_images/', blank=True, null=True)
    #video = models.FileField(upload_to='post_videos/', blank=True, null=True)
    likes = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.user.username} - {self.content[:30]}"

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} on Post {self.post.id}"

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    twitter_username = models.CharField(max_length=150, blank=True)
    facebook_username = models.CharField(max_length=150, blank=True)

    def __str__(self):
        return self.user.username

class SocialAccount(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    twitter_handle = models.CharField(max_length=100, blank=True)
    facebook_handle = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"Social accounts for {self.user.username}"
