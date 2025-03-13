from django.contrib import admin


from .models import News,Categories


class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_ed', 'category','updated_ad', 'is_bool')  # Admin panelda ustunlar
    list_filter = ('created_ed', 'is_bool')  # Filtrlash uchun ustunlar
    search_fields = ('title', 'context')  # Qidirish uchun maydonlar
    list_editable = ['is_bool']
admin.site.register(News, NewsAdmin)  # Admin panelga modelni ro‘yxatdan o‘tkazamiz


class CatAdmin(admin.ModelAdmin):
    list_display =('title_name','cat_id')
    list_filter = ('title_name',)
    search_fields = ('title_name',)



admin.site.register(Categories,CatAdmin)