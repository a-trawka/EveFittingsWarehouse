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
        ('sisters', 'Sisters Of EVE'),
        ('triglavian', 'Triglavian Collective')
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
    name = models.TextField('Hull name', unique=True, max_length=40)
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
    power = models.IntegerField('Powergrid [MW]')
    cpu = models.IntegerField('CPU [tf]')
    capacitor = models.IntegerField('Capacitor [GJ]')

    def __str__(self):
        return self.name


class Module(models.Model):
    SLOT_CHOICES = (
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High')
    )
    TIER_CHOICES = (
        ('1', 'I'),
        ('2', 'II'),
        ('1.1', 'Meta 1'),
        ('1.2', 'Meta 2'),
        ('1.3', 'Meta 3'),
        ('1.4', 'Meta 4'),
        ('story', 'Storyline'),
        ('faction', 'Faction'),
        ('deadspace', 'Deadspace'),
        ('officer', 'Officer')
    )
    name = models.TextField('Module name', unique=True)
    activation_cost = models.IntegerField('Activation cost [GJ]', default=0)
    duration = models.IntegerField('Duration [s]', default=0)
    slot = models.TextField(choices=SLOT_CHOICES)
    tier = models.TextField(choices=TIER_CHOICES)
    required_cpu = models.IntegerField('CPU [tf]')
    required_power = models.IntegerField('Powergrid [MW]')

    def __str__(self):
        return self.name


class Rig(models.Model):
    SIZE_CHOICES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('C', 'Capital')
    )
    name = models.TextField('Rig name')
    size = models.TextField(choices=SIZE_CHOICES)
    calibration = models.IntegerField('Calibration cost')
    drawback = models.IntegerField('Drawback [%]')


class Fitting(models.Model):
    name = models.TextField('Fitting name')
    hull = models.ForeignKey(Hull, on_delete=models.PROTECT)
    # TODO modules
