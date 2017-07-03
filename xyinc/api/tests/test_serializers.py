from rest_framework.test import APITestCase
from xyinc.api.serializers import PoiSerializer


class TestSerializers(APITestCase):
    def setUp(self):
        self.poi = {'name': 'Test poi', 'x':'10', 'y':'20'}

    def test_poi_serializer(self):
        serializer = PoiSerializer(data=self.poi)
        serializer.is_valid()
        self.assertIn('name', serializer.data)

    def test_poi_serializer_valid_data(self):
        serializer = PoiSerializer(data=self.poi, many=False)
        self.assertTrue(serializer.is_valid())

    def test_poi_serializer_invalid_data(self):
        data = {'name': 'Test poi', 'x': -1, 'y': 20}
        serializer = PoiSerializer(data=data)
        self.assertFalse(serializer.is_valid())

    def test_poi_serializer_x_invalid_data_errors(self):
        data = {'name': 'Test poi', 'x': '-1', 'y': '20'}
        serializer = PoiSerializer(data=data)
        serializer.is_valid()
        self.assertIn("{'x': ['Must be a positive number']", str(serializer.errors))

    def test_poi_serializer_y_invalid_data_errors(self):
        data = {'name': 'Test poi', 'x': '10', 'y': '-10'}
        serializer = PoiSerializer(data=data)
        serializer.is_valid()
        self.assertIn("{'y': ['Must be a positive number']", str(serializer.errors))

    def test_poi_serializer_without_coordinate(self):
        data = {'name': 'Test poi', 'x': None, 'y': '-10'}
        serializer = PoiSerializer(data=data)
        serializer.is_valid()
        self.assertIn("'x': ['This field may not be null.']", str(serializer.errors))