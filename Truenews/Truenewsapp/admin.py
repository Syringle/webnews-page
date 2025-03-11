from django.contrib import admin
from .models import NewsCategory, News, Comment, Author

# Register your models here.

# Отображаем дату добавления в списке категорий
class NewsCategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at")

# Отображаем дату добавления в списке новостей
class NewsAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at")


admin.site.register(NewsCategory, NewsCategoryAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(Comment)
admin.site.register(Author)