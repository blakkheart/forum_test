from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator


class MyUser(AbstractUser):

    class Role(models.TextChoices):
        USER = 'user', 'User'
        ADMIN = 'admin', 'Admin'
        MODERATOR = 'moderator', 'Moderator'

    username = models.CharField(max_length=50, unique=True, validators=[
                                RegexValidator(regex=r'^[\w.@+-]+\Z')])
    email = models.EmailField(max_length=254, unique=True)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    second_name = models.CharField(max_length=50, blank=True, null=True)
    date_joined = models.DateField(auto_now=False, auto_now_add=True)
    avatar = models.ImageField(
        upload_to='static/avatars/', null=True, blank=True)
    rating = models.IntegerField(default=0)
    role = models.CharField(
        choices=Role.choices, default=Role.USER, max_length=10
    )

    @property
    def is_admin(self):
        return self.role == self.Role.ADMIN

    @property
    def is_moderator(self):
        return self.role == self.Role.MODERATOR

    @property
    def rating(self):
        rating_comment = self.comments.comment_rating
        rating_post = self.posts.post_rating
        return rating_comment + rating_post

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def __str__(self) -> str:
        return self.username
