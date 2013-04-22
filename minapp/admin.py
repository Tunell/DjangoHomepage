from django.contrib import admin
from minapp.models import Post, Comments
from minapp.views import *

class AdminPost(admin.ModelAdmin):
    list_display = ('titel', 'body', 'pub_date')

admin.site.register(Post, AdminPost)    
admin.site.register(Comments)