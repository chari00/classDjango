from django.contrib import admin

from blog.models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_date')

# Register your models here.
admin.site.register(Post, PostAdmin)