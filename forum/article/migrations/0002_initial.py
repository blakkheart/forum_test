# Generated by Django 4.2.4 on 2023-09-08 13:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('article', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='ratingpost',
            name='user',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name='posts',
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to='article.category',
            ),
        ),
        migrations.AddField(
            model_name='post',
            name='tag',
            field=models.ManyToManyField(to='article.tag'),
        ),
        migrations.AddField(
            model_name='comment',
            name='author',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name='comments',
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name='comments',
                to='article.post',
            ),
        ),
        migrations.AddConstraint(
            model_name='ratingpost',
            constraint=models.CheckConstraint(
                check=models.Q(
                    models.Q(('dislike', False), ('like', True)),
                    models.Q(('dislike', True), ('like', False)),
                    models.Q(('dislike', False), ('like', False)),
                    _connector='OR',
                ),
                name='like or dislike for Post model',
            ),
        ),
    ]
