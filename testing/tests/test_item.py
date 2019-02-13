import unittest
from testing.item import Item


class TestItem(unittest.TestCase):

    def setUp(self):
        self.test_item = Item('Arrow', 1)

    def tearDown(self):
        pass

    def test_item(self):
        self.assertEqual(self.test_item.name, 'Arrow')
        self.assertEqual(self.test_item.quantity, 1)

    def test_add_one(self):
        self.test_item.add_one()
        self.assertEqual(self.test_item.quantity, 2)

    def test_minus_one(self):
        self.test_item.minus_one()
        self.assertEqual(self.test_item.quantity, 0)


if __name__ == '__main__':
    unittest.main()
