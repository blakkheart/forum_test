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
        User, on_delete=models.CASCADE, related_name='posts')
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True)
    tag = models.ManyToManyField(Tag)
    published_at = models.DateTimeField(auto_now=False, auto_now_add=True)

    @property
    def post_rating(self):
        likes = self.rating.filter(like=True).count()
        dislikes = self.rating.filter(dislike=True).count()
        return likes - dislikes

    def __str__(self) -> str:
        return self.title


class Comment(models.Model):
    text = models.TextField()
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')

    @property
    def comment_rating(self):
        likes = self.rating.filter(like=True).count()
        dislikes = self.rating.filter(dislike=True).count()
        return likes - dislikes

    def __str__(self) -> str:
        return self.text[:25]


class RatingPost(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='rating')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    like = models.BooleanField(default=False)
    dislike = models.BooleanField(default=False)

    class Meta:
        constraints = [
            models.CheckConstraint(
                name='like or dislike for Post model',
                check=(
                    models.Q(like=True, dislike=False) |
                    models.Q(like=False, dislike=True) |
                    models.Q(like=False, dislike=False)
                )
            ),
            models.UniqueConstraint(
                fields=('user', 'post'), name='rating_once')
        ]

    def __str__(self) -> str:
        rating = False
        if self.like:
            rating = 'like'
        elif self.dislike:
            rating = 'dislike'
        return f'{self.post} - {self.user} - {rating}'


class RatingComment(models.Model):
    comment = models.ForeignKey(
        Comment, on_delete=models.CASCADE, related_name='rating')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    like = models.BooleanField(default=False)
    dislike = models.BooleanField(default=False)

    class Meta:
        constraints = [
            models.CheckConstraint(
                name='like or dislike for Comment model',
                check=(
                    models.Q(like=True, dislike=False) |
                    models.Q(like=False, dislike=True) |
                    models.Q(like=False, dislike=False)
                )
            ),
            models.UniqueConstraint(
                fields=('user', 'comment'), name='rate_once')
        ]

    def __str__(self) -> str:
        return self.post
