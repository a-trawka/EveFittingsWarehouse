from django.db import models

# BIG TODO: define all basic effects (ex. turret tracking +X%, shield capacity +X, etc.)


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
        ('shuttle', 'Shuttle'),
        ('corvette', 'Corvette'),
        ('frigate', 'Frigate'),
        ('cruiser', 'Cruiser'),
        ('bcruiser', 'Battlecruiser'),
        ('bship', 'Battleship'),
        ('capital', 'Capital'),
    )
    name = models.TextField('Hull name', max_length=40)
    hull_class = models.TextField(choices=CLASS_CHOICES)
    faction = models.TextField(choices=FACTION_CHOICES)
    tier = models.IntegerField()

    slots_low = models.IntegerField('Number of low powered slots')
    slots_medium = models.IntegerField('Number of medium powered slots')
    slots_high = models.IntegerField('Number of high powered slots')
    slots_rigs = models.IntegerField('Number of rig slots')

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
    # TODO: effect = ...

    def __str__(self):
        return f'{self.slot}|{self.name}'


class Rig(models.Model):
    SIZE_CHOICES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('C', 'Capital')
    )
    size = models.TextField(choices=SIZE_CHOICES)
    calibration = models.IntegerField('Calibration cost')
    drawback = models.IntegerField('Drawback [%]')
    # TODO: effect = ...
