from django.contrib import admin

from .models import Hull, Module


class HullAdmin(admin.ModelAdmin):
    fields = ['name', 'hull_class', 'faction', 'tier', 'slots_low', 'slots_medium', 'slots_high',
              'slots_rigs', 'launchers', 'turrets', 'drone_capacity', 'drone_bandwith',
              'calibration', 'power', 'cpu', 'capacitor']


class ModuleAdmin(admin.ModelAdmin):
    fields = ['name', 'activation_cost', 'duration', 'slot', 'tier', 'required_cpu', 'required_power']


admin.site.register(Hull, HullAdmin)
admin.site.register(Module, ModuleAdmin)
