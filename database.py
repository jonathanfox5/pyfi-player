import os
import sqlite3

DEFAULT_PATH = os.path.join(os.path.dirname(__file__), "database.sqlite3")


def db_connect(db_path=DEFAULT_PATH):
    db = sqlite3.connect(db_path)
    return db


def db_disconnect(db):
    db.close()


def build_table(db):
    sql = """
        CREATE TABLE tblAlbums(id INTEGER PRIMARY KEY, artist TEXT, album_name TEXT, path TEXT, rfid_id TEXT)
        """
    execute_sql(db, sql)


def delete_table(db):
    sql = """
        DROP TABLE IF EXISTS tblAlbums
        """
    execute_sql(db, sql)


def execute_sql(db, sql, sql_args=None):
    cursor = db.cursor()

    if sql_args == None:
        cursor.execute(sql)
    else:
        x = cursor.execute(sql, sql_args)

        print(x)

    db.commit()


def test_data(db):
    sql = """
        INSERT INTO tblAlbums(artist, album_name)
        VALUES (?,?)
    """

    values = ("Rammstein", "Mutter")

    execute_sql(db, sql, values)


if __name__ == "__main__":
    db = db_connect()
    delete_table(db)
    build_table(db)
    test_data(db)
    delete_table(db)
    db_disconnect(db)
