from django.test import TestCase
from faunatrack.models import Observation

# Create your tests here.
class TestObservation(TestCase):

    def setUp(self):
        self.observations = Observation.objects.all()

    def test_observation_has_espece(self):
        for obs in self.observations:
            self.assertTrue(obs.espece)
