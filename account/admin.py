from django.contrib import admin
from django.utils.safestring import mark_safe  # марк сэйв для картинки профиля

from .models import Profile


admin.site.site_title = 'Fresh Group'


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'get_photo', 'position', 'date_of_birth']
    list_filter = ['user', 'position', 'date_of_birth']
    search_fields = ['user', 'about']
    prepopulated_fields = {'slug': ('user',)}

    # Определяем изображение в админке.
    def get_photo(self, Profile):
        if Profile.photo:
            return mark_safe(f'<img src="{Profile.photo.url}" width="75">')
        else:
            return 'Фото нет'

    get_photo.short_description = 'Фото'
