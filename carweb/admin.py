from django.contrib import admin

from .models import Cars


class CarsAdmin(admin.ModelAdmin):
    list_display = ('id','name','prise','created_ed','updated_ad','is_bool')
    list_display_links = ['name']
    search_fields = ['name']
    list_editable = ['is_bool']



admin.site.register(Cars,CarsAdmin)  

