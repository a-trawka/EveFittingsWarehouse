from django.test import TestCase
from django.urls import reverse

from .models import Hull


def create_hull(name):
    return Hull.objects.create(
        name=name,
        hull_class=Hull.CLASS_CHOICES[0],
        faction=Hull.FACTION_CHOICES[0],
        tier=1,
        slots_low=2,
        slots_medium=2,
        slots_high=3,
        slots_rigs=3,
        launchers=1,
        turrets=1,
        drone_capacity=5,
        drone_bandwith=5,
        calibration=200,
        power=600,
        cpu=500,
        capacitor=800
    )


class HullIndexTestCase(TestCase):

    def test_no_hulls(self):
        response = self.client.get(reverse('fitting:hulls'))
        self.assertQuerysetEqual(response.context['hulls'], [])

    def test_one_hull(self):
        create_hull('Test Hull')
        response = self.client.get(reverse('fitting:hulls'))
        self.assertQuerysetEqual(response.context['hulls'], ['<Hull: Test Hull>'])

    def test_more_than_5_hulls(self):
        for i in range(1, 7):
            create_hull(f'Test Hull {i}')
        response = self.client.get(reverse('fitting:hulls'))
        expected_qs = [f'<Hull: Test Hull {i}>' for i in range(1, 6)]
        self.assertQuerysetEqual(response.context['hulls'], expected_qs, ordered=False)
