from rest_framework.test import APITestCase


class APITests(APITestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_index(self):
        """ Must test index return status code 200 """
        resp = self.client.get('/api/v0/')
        self.assertEqual(200, resp.status_code)

    def test_pois_get(self):
        """ Must test pois return status code 200 """
        resp = self.client.get('/api/v0/pois/')
        self.assertEqual(200, resp.status_code)
