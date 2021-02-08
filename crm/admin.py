from django.contrib import admin

from .models import Client, Comment, Category


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
	# Отображаемые поля в админке
	list_display = ['title', 'decision_maker', 'phone', 'email']
	# Поля, по которым можно фильтровать
	list_filter = ['title', 'decision_maker', 'responsible']
	# Поиск по полям
	search_fields = ['title', 'decision_maker']
	# Ссылка автоматически заполняется
	prepopulated_fields = {'slug': ('title',)}


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
	list_display = ['id', 'author', 'created', 'updated']
	list_filter = ['author', 'created', 'updated']
	search_fields = ['text']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
	list_display = ['name', 'slug']
	prepopulated_fields = {'slug': ('name',)}
