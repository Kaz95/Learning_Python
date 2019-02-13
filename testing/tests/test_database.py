import unittest
from testing.database import create_connection


class TestDatabase(unittest.TestCase):

    def test_create_connection(self):
        self.assertIsNotNone(create_connection(':memory:'))


if __name__ == '__main__':
    unittest.main()

