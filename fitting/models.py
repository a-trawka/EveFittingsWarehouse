from django.db import models


class Hull(models.Model):
    FACTION_CHOICES = (
        ('amarr', 'Amarr Empire'),
        ('caldari', 'Caldari State'),
        ('gallente', 'Gallente Federation'),
        ('minmatar', 'Minmatar Republic'),
        ('angel', 'Angel Cartel'),
        ('blood', 'Blood Raiders'),
        ('guristas', 'Guristas'),
        ('mordu', "Mordu's Legion"),
        ('sansha', "Sansha's Nation"),
        ('serpentis', 'Serpentis'),
        ('sisters', 'Sisters Of EVE')
    )
    CLASS_CHOICES = (
        ('shuttle', 'SHUTTLE'),
        ('frigate', 'FRIGATE'),
        ('cruiser', 'CRUISER'),
        # TODO
    )
    name = models.TextField('Hull name', max_length=40)
    hull_class = models.TextField(choices=CLASS_CHOICES)
    faction = models.TextField(choices=FACTION_CHOICES)
    tier = models.IntegerField()

    slots_low = models.IntegerField('Number of low powered slots')
    slots_medium = models.IntegerField('Number of medium powered slots')
    slots_high = models.IntegerField('Number of high powered slots')
    slots_rigs = models.IntegerField('Number of rig slots')  # TODO: distinct size of rigs (choices ex. LARGE_3, MED_2)

    launchers = models.IntegerField('Max mounted launchers')
    turrets = models.IntegerField('Max mounted turrets')
    drone_capacity = models.IntegerField()
    drone_bandwith = models.IntegerField()

    calibration = models.IntegerField()
    power = models.IntegerField('Powergrid')
    cpu = models.IntegerField('CPU')
    capacitor = models.IntegerField('Capacitor')

    def __str__(self):
        return self.name


class Fitting(models.Model):
    name = models.TextField('Fitting name')
    hull = models.ForeignKey(Hull, on_delete=models.PROTECT)


class Module(models.Model):
    SLOT_CHOICES = (
        ('low', 'LOW'),
        ('medium', 'MEDIUM'),
        ('high', 'HIGH')
    )
    fitting = models.ManyToManyField(Fitting)
    name = models.TextField('Module name')
    slot = models.TextField(choices=SLOT_CHOICES)
    required_cpu = models.IntegerField('CPU')
    required_power = models.IntegerField('Powergrid')

    def __str__(self):
        return f'{self.slot}|{self.name}'
