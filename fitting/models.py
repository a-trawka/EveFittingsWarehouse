from django.db.models import Model, TextField, IntegerField


class Module(Model):
    SLOT_CHOICES = ('low', 'medium', 'high')
    name = TextField('Module name')
    slot = TextField(choices=SLOT_CHOICES)
    required_cpu = IntegerField('CPU')
    required_power = IntegerField('Powergrid')


class Hull(Model):
    FACTION_CHOICES = ('ammar', 'caldari', 'gallente', 'minmatar')  # TODO: pirate factions
    name = TextField('Hull name')
    faction = TextField(choices=FACTION_CHOICES)

    slots_low = IntegerField('Number of low powered slots')
    slots_medium = IntegerField('Number of medium powered slots')
    slots_high = IntegerField('Number of high powered slots')
    slots_rigs = IntegerField('Number of rig slots')  # TODO: distinct size of rigs (choices ex. LARGE_3, MED_2)

    launchers = IntegerField('Max mounted launchers')
    turrets = IntegerField('Max mounted turrets')
    drone_capacity = IntegerField()
    drone_bandwith = IntegerField()

    calibration = IntegerField()
    power = IntegerField('Powergrid')
    cpu = IntegerField('CPU')
    capacitor = IntegerField('Capacitor')
    