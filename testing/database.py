import sqlite3
from sqlite3 import Error
import testing.sql

db = 'C:\\sqlite\\db\\test.db'
mem = ':memory:'


# TODO refactor to not hard code database path. Will not work for others trying to use codebase.
# Creates a connection to test.db
def create_connection(db_path):
    try:
        conn = sqlite3.connect(db_path)
        return conn
    except Error as e:
        print(e)
    return None


# Verifies store item count via sqlite count(*) method which returns row count for a given table.
# Not currently used.
# def wrong_item_count():
#     store_item_count = 256
#     con = create_connection(mem)
#     with con:
#         cursor = con.cursor()
#         cursor.execute("SELECT count(*) FROM items;")
#         cur_item_count = cursor.fetchone()
#         cur_item_count = cur_item_count[0]
#         if cur_item_count == store_item_count:
#             return False
#         else:
#             return True

# SQL statements


# def execute_sql_2(con, sql_statement, var=None):
#     cur = con.cursor()
#     cur.execute(sql_statement, var)


# def execute_fetchone_sql_2(con, sql_statement, var=None):
#     cur = con.cursor()
#     if var is not None:
#         cur.execute(sql_statement, var)
#     else:
#         cur.execute(sql_statement)
#
#     return cur.fetchone()


# def execute_fetchall_sql_2(con, sql_statement, var=None):
#     cur = con.cursor()
#     if var is not None:
#         cur.execute(sql_statement, var)
#     else:
#         cur.execute(sql_statement)
#
#     return cur.fetchall()


# INSERT

# Inserts given values into accounts table at given columns. Returns last row id.
def add_account_row(conn, some_account):
    sql = """INSERT INTO accounts (username, password)
            VALUES(?,?)"""

    testing.sql.execute_sql(conn, sql, some_account[0], some_account[1])
    # cursor = conn.cursor()
    # cursor.execute(sql, some_account)
    return sql


# Inserts given values into accounts table at given columns. Returns last row id.
def add_inventory_row(conn, some_inventory):
    sql = """INSERT INTO inventories (character_id, name)
            VALUES(?,?)"""
    testing.sql.execute_sql(conn, sql, some_inventory[0], some_inventory[1])
    return sql


# Inserts given values into accounts table at given columns. Returns last row id.
def add_character_row(conn, some_character):
    sql = """INSERT INTO characters (account_id, name, currency)
            VALUES(?,?,?)"""
    testing.sql.execute_sql(conn, sql, some_character[0], some_character[1], some_character[2])
    return sql


# Inserts given values into accounts table at given columns. Returns last row id.
def add_item_row(conn, some_item):
    sql = """INSERT INTO items (inventory_id, item, api, quantity)
            VALUES(?,?,?,?)"""
    testing.sql.execute_sql(conn, sql, some_item[0], some_item[1], some_item[2], some_item[3])
    return sql


# Used to populate stores
def add_store_item(con, item_info):
    sql = """INSERT INTO items (item, api, store)
             VALUES(?,?,?)"""
    testing.sql.execute_sql(con, sql, item_info[0], item_info[1], item_info[2])
    return sql


# QUERY
def query_fetchone(conn, sql):
    return testing.sql.execute_fetchone_sql(conn, sql)


def query_fetchall(conn, sql):
    return testing.sql.execute_fetchall_sql(conn, sql)


def query_fetchone_list(conn, sql, var):
    return list(testing.sql.execute_fetchone_sql(conn, sql, var))


def query_fetchall_list(conn, sql, var):
    return list(testing.sql.execute_fetchall_sql(conn, sql, var))


# def query_username_password(conn, sql):
#     # sql = """SELECT username, password FROM accounts;"""
#     some_account = execute_fetchall_sql(conn, sql)
#     return some_account
#
#
# def query_account_row(conn, sql, username):
#     # sql = """SELECT id, username, password FROM accounts WHERE username = ?;"""
#     some_account = execute_fetchone_sql(conn, sql, username)
#     return list(some_account)
#
#
# def query_character_row(conn, sql, character_name):
#     # sql = """SELECT id, name, currency FROM characters WHERE name = ?;"""
#     some_account = execute_fetchone_sql(conn, sql, character_name)
#     return list(some_account)
#
#
# def query_inventory_row(conn, sql, inventory_name):
#     # sql = """SELECT id, name FROM inventories WHERE name = ?;"""
#     some_account = execute_fetchone_sql(conn, sql, inventory_name)
#     return list(some_account)
#
#
# def query_all_characters(conn, sql, account_id):
#     # sql = """SELECT name, currency FROM characters WHERE account_id = ?;"""
#     some_account = execute_fetchall_sql(conn, sql, account_id)
#     for character in some_account:
#         print(list(character))
#
#
# def query_all_inventories(conn, sql, character_id):
#     # sql = """SELECT name FROM inventories WHERE character_id = ?;"""
#     some_account = execute_fetchall_sql(conn, sql, character_id)
#     for character in some_account:
#         print(list(character))

# TODO test
def query_accounts_with_characters(conn, sql):
    temp = []
    # sql = """SELECT DISTINCT account_id FROM characters;"""
    account_id_list = testing.sql.execute_fetchall_sql(conn, sql)
    for tup in account_id_list:
        temp.append(tup[0])
    return temp


# TODO test
def query_characters_with_inventories(conn,  sql):
    temp = []
    # sql = """SELECT DISTINCT character_id FROM inventories;"""
    account_id_list = testing.sql.execute_fetchall_sql(conn, sql)
    for tup in account_id_list:
        temp.append(tup[0])
    return temp


# SELECT

# TODO decouple sql and test....maybe?
def count_rows(conn, some_table):
    sql = """SELECT count(*) FROM {};""".format(some_table)
    yup = testing.sql.execute_fetchone_sql(conn, sql)
    return yup[0]


if __name__ == '__main__':
    acc = ('username', 'password')
    inv = (1, 'inv name')
    char = (1, 'char name', 420)
    item = (1, 'item name', 'api url', 1)
    con = create_connection(db)
    with con:
        print(add_account_row(con, acc))
        add_inventory_row(con, inv)
        add_character_row(con, char)
        add_item_row(con, item)

        # modular queries
        print(query_fetchall(con, testing.sql.sql_username_password()))
        print(query_fetchone_list(con, testing.sql.sql_account_row(), acc[0]))
        print(query_fetchone_list(con, testing.sql.sql_character_row(), char[1]))
        print(query_fetchone_list(con, testing.sql.sql_inventory_row(), inv[1]))
        print(query_fetchall_list(con, testing.sql.sql_all_characters(), 1))

        # Use these as reference for new queries

        # print(query_username_password(con, sql_username_password()))
        # print(query_account_row(con, sql_account_row(), 'Kazact'))
        # print(query_character_row(con, sql_character_row(), 'char name'))
        # print(query_inventory_row(con, sql_inventory_row(), 'Kazact'))
        # print(query_all_characters(con, sql_all_characters(), '1'))

        # print(query_accounts_with_characters(con, sql_accounts_with_characters()))
        # print(query_characters_with_inventories(con, sql_characters_with_inventories()))
        # print(query_all_inventories(con, sql_all_inventories(), 1))
        # print(count_rows(con, 'items'))
    # # stock_stores()
