from django.contrib import admin

from .models import *


class CitiesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'long', 'lat')
    search_fields = ('title', 'stores')


class StoresAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'city', 'address', 'phone', 'email', 'website')
    search_fields = ('title', 'city')


admin.site.register(Stores, StoresAdmin)
admin.site.register(Cities, CitiesAdmin)

