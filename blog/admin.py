from django.contrib import admin
from blog.models import Post

@admin.register(Post)
class PageAdmin(admin.ModelAdmin):
    list_display = ['title',]
