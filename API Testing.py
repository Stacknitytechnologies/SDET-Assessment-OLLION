import requests
import unittest

class TestStackExchangeBadgesAPI(unittest.TestCase):
    base_url = "https://api.stackexchange.com/"

    def setUp(self):
        # Replace 'YOUR_ACCESS_TOKEN' with the actual access token obtained from Step 1
        self.access_token = '5pJtDBsE0Sk*5kflX9TfbA))'

    def test_badges_api_ids(self):
        url = f"{self.base_url}/2.3/badges/{self}?order=desc&sort=rank&site=stackoverflow"
        params = {'site': 'stackoverflow', 'access_token': self.access_token, 'filter': '!9Z9z5(1'}
        response = requests.get(url, params=params)

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), dict)
        self.assertIn('items', response.json())
        self.assertIsInstance(response.json()['items'], list)

    def test_badges_api_recipients(self):
        url = f"{self.base_url}/2.3/badges/recipients?site=stackoverflow"
        params = {'site': 'stackoverflow', 'access_token': self.access_token, 'page': 1, 'pagesize': 10, 'order': 'desc', 'sort': 'creation'}
        response = requests.get(url, params=params)

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), dict)
        self.assertIn('items', response.json())
        self.assertIsInstance(response.json()['items'], list)
        self.assertLessEqual(len(response.json()['items']), 10)

    def test_badges_api_tags(self):
        url = f"{self.base_url}/2.3/badges/tags?order=desc&sort=rank&site=stackoverflow"
        params = {'site': 'stackoverflow', 'access_token': self.access_token, 'page': 1, 'pagesize': 10, 'order': 'desc', 'sort': 'popular'}
        response = requests.get(url, params=params)

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), dict)
        self.assertIn('items', response.json())
        self.assertIsInstance(response.json()['items'], list)
        self.assertLessEqual(len(response.json()['items']), 10)

if __name__ == "__main__":
    unittest.main()