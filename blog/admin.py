from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Category, Post, Tag

# admin.site.register(Category)
# admin.site.register(Post)
# admin.site.register(Tag)


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'creat_time', 'modify_time', 'category', 'author']

admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)
