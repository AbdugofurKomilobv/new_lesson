from django.contrib import admin


from .models import News


class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_ed', 'updated_ad', 'is_bool')  # Admin panelda ustunlar
    list_filter = ('created_ed', 'is_bool')  # Filtrlash uchun ustunlar
    search_fields = ('title', 'context')  # Qidirish uchun maydonlar

admin.site.register(News, NewsAdmin)  # Admin panelga modelni ro‘yxatdan o‘tkazamiz
