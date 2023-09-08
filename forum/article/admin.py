from django.contrib import admin

from article.models import Post, Comment, RatingPost, Category, Tag, RatingComment


admin.site.register(Comment)
admin.site.register(RatingPost)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(RatingComment)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    fieldsets = (
        (
            'Standard info',
            {
                'fields': (
                    'title',
                    'text_body',
                    'author',
                    'category',
                    'tag',
                    'published_at',
                )
            },
        ),
        ('Extra Fields', {'fields': ('post_rating',)}),
    )
    readonly_fields = ('post_rating', 'published_at',)
