import unittest
from unittest.mock import patch
from testing.database import create_connection
from testing.database import add_account_row, add_inventory_row, add_item_row, add_character_row, add_store_item


class TestDatabase(unittest.TestCase):

    # def test_create_connection(self):
        # self.assertIsNotNone(create_connection(':memory:'))

    def test_create_connection(self):
        with patch('testing.database.sqlite3.connect') as mocksql:
            mocksql.return_value = 'Success'
            self.assertEqual(create_connection(':memory:'), 'Success')

    def test_add_account_row(self):
        with patch('testing.database.sqlite3') as mocksql:
            conn = mocksql.connect()
            self.assertEqual(add_account_row(conn, [1, 2]), """INSERT INTO accounts (username, password)
            VALUES(?,?)""")

    def test_add_inventory_row(self):
        with patch('testing.database.sqlite3') as mocksql:
            conn = mocksql.connect()
            self.assertEqual(add_inventory_row(conn, [1, 2]), """INSERT INTO inventories (character_id, name)
            VALUES(?,?)""")

    def test_add_character_row(self):
        with patch('testing.database.sqlite3') as mocksql:
            conn = mocksql.connect()
            self.assertEqual(add_character_row(conn, [1, 2, 3]), """INSERT INTO characters (account_id, name, currency)
            VALUES(?,?,?)""")

    def test_add_item_row(self):
        with patch('testing.database.sqlite3') as mocksql:
            conn = mocksql.connect()
            self.assertEqual(add_item_row(conn, [1, 2, 3, 4]), """INSERT INTO items (inventory_id, item, api, quantity)
            VALUES(?,?,?,?)""")

    def test_add_store_item(self):
        with patch('testing.database.sqlite3') as mocksql:
            conn = mocksql.connect()
            self.assertEqual(add_store_item(conn, [1, 2, 3]), """INSERT INTO items (item, api, store)
             VALUES(?,?,?)""")


if __name__ == '__main__':
    unittest.main()

