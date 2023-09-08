# Generated by Django 4.2.4 on 2023-09-08 13:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('article', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RatingComment',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                ('like', models.BooleanField(default=False)),
                ('dislike', models.BooleanField(default=False)),
            ],
        ),
        migrations.AlterField(
            model_name='ratingpost',
            name='post',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name='rating',
                to='article.post',
            ),
        ),
        migrations.AddConstraint(
            model_name='ratingpost',
            constraint=models.UniqueConstraint(
                fields=('user', 'post'), name='rating_once'
            ),
        ),
        migrations.AddField(
            model_name='ratingcomment',
            name='comment',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name='rating',
                to='article.comment',
            ),
        ),
        migrations.AddField(
            model_name='ratingcomment',
            name='user',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddConstraint(
            model_name='ratingcomment',
            constraint=models.CheckConstraint(
                check=models.Q(
                    models.Q(('dislike', False), ('like', True)),
                    models.Q(('dislike', True), ('like', False)),
                    models.Q(('dislike', False), ('like', False)),
                    _connector='OR',
                ),
                name='like or dislike for Comment model',
            ),
        ),
        migrations.AddConstraint(
            model_name='ratingcomment',
            constraint=models.UniqueConstraint(
                fields=('user', 'comment'), name='rate_once'
            ),
        ),
    ]
