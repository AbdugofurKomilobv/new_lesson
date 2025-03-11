from django.contrib import admin

from .models import Cars

# class NewCars(admin.ModelAdmin):

admin.site.register(Cars)  # Admin panelga modelni ro‘yxatdan o‘tkazamiz

