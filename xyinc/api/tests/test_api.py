import json
from rest_framework import status
from rest_framework.test import APITestCase


class APITests(APITestCase):
    def test_index(self):
        """ Index test must return status code 200 """
        resp = self.client.get('/api/v0/')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)


class APITestPoi(APITestCase):
    def setUp(self):
        self.resouce_url = '/api/v0/pois/'
    def test_pois_get(self):
        """ Pois test must return status code 200 """
        resp = self.client.get(self.resouce_url)
        self.assertEqual(200, resp.status_code)
        self.assertEqual(str([]), str(resp.data))

    def test_create_poi(self):
        """ Poi create test must return status 201 and data"""
        data = {'name': 'test post', 'x': 10, 'y': 15}
        resp = self.client.post(self.resouce_url, data=data, format='json')
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)
        self.assertEqual(str(resp.data), str(data))

    def test_create_poi_with_name_none(self):
        data = {'name': None, 'x': 10, 'y': 15}
        resp = self.client.post(self.resouce_url, data=data, format='json')
        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual({'name': ['This field may not be null.']}, json.loads(resp.content))

    def test_create_poi_with_x_none(self):
        data = {'name': 'Test poi', 'x': None, 'y': 15}
        resp = self.client.post(self.resouce_url, data=data, format='json')
        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual({'x': ['This field may not be null.']}, json.loads(resp.content))

    def test_create_poi_with_y_none(self):
        data = {'name': 'Test poi', 'x': 10, 'y': None}
        resp = self.client.post(self.resouce_url, data=data, format='json')
        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual({'y': ['This field may not be null.']}, json.loads(resp.content))

    def test_create_poi_without_name(self):
        data = {'x': 10, 'y': 15}
        resp = self.client.post(self.resouce_url, data=data, format='json')
        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual({'name': ['This field is required.']}, json.loads(resp.content))

    def test_create_poi_without_x(self):
        data = {'name': 'Test poi', 'y': 15}
        resp = self.client.post(self.resouce_url, data=data, format='json')
        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual({'x': ['This field is required.']}, json.loads(resp.content))

    def test_create_poi_without_y(self):
        data = {'name': 'Test poi', 'x': 10}
        resp = self.client.post(self.resouce_url, data=data, format='json')
        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual({'y': ['This field is required.']}, json.loads(resp.content))


class APITestPoiRadius(APITestCase):
    def setUp(self):
        self.xyin_pois = [{'name': 'Lanchonete', 'x': 27, 'y': 12},
                          {'name': 'Posto', 'x': 31, 'y': 18},
                          {'name': 'Joalheria', 'x': 15, 'y': 12},
                          {'name': 'Floricultura', 'x': 19, 'y': 21},
                          {'name': 'Pub', 'x': 12, 'y': 8},
                          {'name': 'Supermercado', 'x': 23, 'y': 6},
                          {'name': 'Churrascaria', 'x': 28, 'y': 2},
                          ]

    def test_search_poi_by_radius(self):
        pois = [{'name': 'poi1', 'x': 10, 'y': 10},
                {'name': 'poi2', 'x': 20, 'y': 30},
                {'name': 'poi3', 'x': 14, 'y': 17},
                ]

        for poi in pois:
            self.client.post('/api/v0/pois/', data=poi)

        data = {'x': 5, 'y': 8, 'd-max': 10}
        resp = self.client.get('/api/v0/pois/search/', data=data, format='json')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(resp.content)[0], pois[0])

    def test_search_all_params(self):

        for poi in self.xyin_pois:
            self.client.post('/api/v0/pois/', data=poi)

        query = {'x': 20, 'y': 10, 'd-max': 10}

        expected_results = [{'name': 'Lanchonete', 'x': 27, 'y': 12},
                            {'name': 'Joalheria', 'x': 15, 'y': 12},
                            {'name': 'Pub', 'x': 12, 'y': 8},
                            {'name': 'Supermercado', 'x': 23, 'y': 6},
                            ]
        resp = self.client.get('/api/v0/pois/search/', data=query, format='json')
        self.assertJSONEqual(resp.content, expected_results)


    def test_xyinc_withou_params(self):
        for poi in self.xyin_pois:
            self.client.post('/api/v0/pois/', data=poi)

        query = {'y': 10, 'd-max': 10}
        resp = self.client.get('/api/v0/pois/search/', data=query, format='json')
        self.assertEqual(json.loads(resp.content), [])