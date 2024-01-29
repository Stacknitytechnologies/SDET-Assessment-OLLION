import unittest
import json
import requests
class TestStackExchangeBadgesAPI(unittest.TestCase):
    base_url = "https://stackoverflow.com/oauth/login_success"

    def setUp(self):
        self.access_token = '5pJtDBsE0Sk*5kflX9TfbA))'

    def test_badges_api_ids(self):
        url = f"{self.base_url}/2.3/badges/{self.access_token}?order=desc&sort=rank&site=stackoverflow"
        params = {'site': 'stackoverflow', 'filter': '!9Z9z5(1'}
        response = requests.get(url, params=params)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(json.loads(response.text), dict)
        self.assertGreaterEqual(len(json.loads(response.text)['items']), 1)

    def test_badges_api_recipients(
            self):
        url = f"{self.base_url}/2.3/badges/recipients?site=stackoverflow" 
        params = {'site': 'stackoverflow', 'access_token': self.access_token, 'page': 1, 'pagesize': 10, 'order': 'desc', 'sort': 'creation'} 
        response = requests.get(url, params=params)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(json.loads(response.text), dict)
        self.assertLessEqual(len(json.loads(response.text)['items']), 10)
        self.assertGreaterEqual(len(json.loads(response.text)['items']), 1)

    def test_badges_api_tags(self): 
        url = f"{self.base_url}/2.3/badges/tags?order=desc&sort=rank&site=stackoverflow" 
        params = {'site': 'stackoverflow', 'access_token': self.access_token, 'page': 1, 'pagesize': 10, 'order': 'desc', 'sort': 'popular'} 
        response = requests.get(url, params=params)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(json.loads(response.text), dict)
        self.assertLessEqual(len(json.loads(response.text)['items']), 10)
        self.assertGreaterEqual(len(json.loads(response.text)['items']), 1)
if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(TestStackExchangeBadgesAPI('test_badges_api_ids'))
    suite.addTest(TestStackExchangeBadgesAPI('test_badges_api_recipients'))
    suite.addTest(TestStackExchangeBadgesAPI('test_badges_api_tags'))
    runner = unittest.TextTestRunner()
    runner.run(suite)