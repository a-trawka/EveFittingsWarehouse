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


class HullsTestCase(TestCase):

    def test_no_hulls(self):
        response = self.client.get(reverse('fitting:hulls'))
        self.assertEqual(response.status_code, 404)

    def test_one_hull(self):
        create_hull('Test Hull')
        response = self.client.get(reverse('fitting:hulls'))
        self.assertEqual('Test Hull', response.json()[0]['fields']['name'])

    def test_list_of_hulls(self):
        for i in range(1, 7):
            create_hull(f'Test Hull {i}')
        response = self.client.get(reverse('fitting:hulls'))
        self.assertEqual(len(response.json()), 6)
        self.assertEqual('Test Hull 1', response.json()[0]['fields']['name'])
        self.assertEqual('Test Hull 2', response.json()[1]['fields']['name'])
        self.assertEqual('Test Hull 3', response.json()[2]['fields']['name'])


class HullTestCase(TestCase):

    def test_valid_hull(self):
        valid_hull = create_hull('Test Hull')
        response = self.client.get(reverse('fitting:hull', args=(valid_hull.id,)))
        self.assertContains(response, valid_hull.name)

    def test_wrong_id(self):
        response = self.client.get(reverse('fitting:hull', args=(10,)))
        self.assertEqual(response.status_code, 404)

# TODO: Modules View Case
