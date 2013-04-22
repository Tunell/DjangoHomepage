from django.contrib import admin
from sidan.models import News
from sidan.views import *

class AdminNews(admin.ModelAdmin):
    list_display = ('titel', 'body', 'pub_date')

admin.site.register(News, AdminNews)