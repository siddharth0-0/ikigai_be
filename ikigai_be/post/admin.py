from django.contrib import admin
from .models import Post, Mood


class PostAdmin(admin.ModelAdmin):
    list_display = ('post_id', 'post_text', 'user_id', 'mood_id')


class MoodAdmin(admin.ModelAdmin):
    list_display = ('mood_id', 'mood_type')


admin.site.register(Mood)
admin.site.register(Post, PostAdmin)
