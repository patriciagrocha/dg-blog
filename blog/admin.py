from django.contrib import admin
from .models import Post

# admin.site.register(Post)

# mesmo resultado porém com mais liberdade 
@admin.register(Post)
class Post(admin.ModelAdmin):
    list_display = ("author", "title", "text", "created_date", "published_date")
