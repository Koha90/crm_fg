from django.contrib import admin

from .models import Client


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
