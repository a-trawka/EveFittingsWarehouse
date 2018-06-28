from django.contrib import admin

from .models import Hull


class HullAdmin(admin.ModelAdmin):
    fields = ['name', 'hull_class', 'faction', 'tier', 'slots_low', 'slots_medium', 'slots_high',
              'slots_rigs', 'launchers', 'turrets', 'drone_capacity', 'drone_bandwith',
              'calibration', 'power', 'cpu', 'capacitor']


admin.site.register(Hull, HullAdmin)
