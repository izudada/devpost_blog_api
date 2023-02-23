from django.contrib import admin

from .models import Article, Comment


class CommentInline(admin.TabularInline):
    model = Comment


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title',)
    inlines = [CommentInline]


admin.site.register(Article, ArticleAdmin)
