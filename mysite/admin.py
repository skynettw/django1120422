from django.contrib import admin

from mysite.models import News, BodyInfo

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'source', 'pdate')

@admin.register(BodyInfo)
class BodyInfoAdmin(admin.ModelAdmin):
    list_display = ('name', 'height', 'weight')
