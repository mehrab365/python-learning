from django.contrib import admin


# Register your models here.
from posts.models import Post

class PostModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'timestamp','id']
    list_display_links = ['content','timestamp']
    list_filter = ['title','timestamp']
    list_editable = ['title']
    
    search_fields = ['title', 'content']
#     list
    class Meta:
        model = Post

admin.site.register(Post,PostModelAdmin)