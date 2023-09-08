from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name


class Category(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=50)
    text_body = models.TextField()
    author = models.ForeignKey(
        User, on_delete=models.SET_NULL, related_name='posts')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL)
    tag = models.ManyToManyField(Tag)
    published_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    likes = models.ManyToManyField(User, blank=True, related_name='likes')
    dislikes = models.ManyToManyField(
        User, blank=True, related_name='dislikes')

    def get_likes(self, obj):
        likes = obj.likes.all().count()
        dislikes = obj.dislikes.all().count()
        return (likes-dislikes)

    def __str__(self) -> str:
        return self.title


class Comment(models.Model):
    text = models.TextField()
    author = models.ForeignKey(
        User, on_delete=models.SET_NULL, related_name='comments')
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')

    def __str__(self) -> str:
        return self.text[:25]
