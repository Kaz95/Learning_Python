import unittest
from unittest.mock import patch
from testing.api import call_api, convert_json_slice_dict, search


class TestApi(unittest.TestCase):

    def test_call_api(self):
        with patch('testing.api.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'Success'

            response = call_api('http://www.dnd5eapi.co/api/equipment/')
            # mocked_get.assert_called_with('http://www.dnd5eapi.co/api/equipment/')
            self.assertEqual(response, 'Success')

    def test_convert_json_slice_dict(self):
        api_call = '{"results": 1}'
        self.assertEqual(convert_json_slice_dict(api_call), 1)

    def test_search(self):
        list_of_dicts = '{"results": [{"name": 1, "url": 1},{"name": 2, "url": 2}]}'
        self.assertEqual(search(1, list_of_dicts), [1, 1])




if __name__ == '__main__':
    unittest.main()
