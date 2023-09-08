from django.contrib import admin

from django.contrib.auth import get_user_model

User = get_user_model()


@admin.register(User)
class PostAdmin(admin.ModelAdmin):
    fieldsets = (
        (
            'Standard info',
            {
                'fields': (
                    'username',
                    'password',
                    'email',
                    'first_name',
                    'last_name',
                    'date_joined',
                )
            },
        ),
        ('Extra Fields', {'fields': ('role', 'rating')}),
    )
    readonly_fields = ('date_joined', 'rating',)
