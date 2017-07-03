from django.db.models import QuerySet
from django.test import TestCase
from rest_framework.exceptions import ValidationError

from xyinc.api.models import Poi


class APIModelTest(TestCase):
    def setUp(self):
        self.name, self.x, self.y = "Test poi", "10", "12"
        self.obj = Poi.create(name=self.name, x=self.x, y=self.y)
        self.obj.save()

    def tearDown(self):
        pass

    def test_create_poi(self):
        self.assertIsInstance(self.obj, Poi)

    def test_retrieve_all_pois(self):
        obj_all = Poi.get()
        self.assertIsInstance(obj_all, QuerySet)

    def test_retrieve_one_poi_by_name(self):
        obj = Poi.get(name=self.name)
        self.assertIsInstance(obj, Poi)

    def test_retrieve_one_poi_non_name(self):
        obj = Poi.get(name='error')
        self.assertEqual(obj, None)

    def test_retrieve_only_x_coordinate(self):
        with self.assertRaises(ValidationError) as ex:
            obj = Poi.get(x='10')

        self.assertIn('Must be x,y coordinates', str(ex.exception))

    def test_retrieve_only_y_coordinate(self):
        with self.assertRaises(ValidationError) as ex:
            obj = Poi.get(y='10')

        self.assertIn('Must be x,y coordinates', str(ex.exception))

    def test_poi_str(self):
        self.assertEqual('Test poi (10, 12)', str(self.obj))
