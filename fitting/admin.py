from django.contrib import admin

from .models import Hull, Fitting, Module


class HullAdmin(admin.ModelAdmin):
    fields = ['name', 'faction', 'tier']


admin.site.register(Hull, HullAdmin)