import sqlite3
import rsa

def encrypt(text, pub, priv):
    pass

def decrypt(text, privkey):
    pass

def connect_database():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    return conn, cursor

def database_initalise(connection, cursor):
    cursor.execute("CREATE TABLE IS NOT EXISTS passwords (PASSWORD  TEXT    NOT NULL)")
    connection.commit()
    return 0

def gen_keys():
    pub, priv = rsa.newkeys()
    return pub, priv

def add_passwords(password, connection, cursor, pubkey):
    enc = encrypt(password, pubkey)
    cursor.execute("INSERT INTO passwords (PASSWORD) VALUES (?)", (enc))
    connection.commit()
    return 0

def read_database(cursor, connection, privkey):
    records = cursor.execute("SELECT * FROM passwords")
    for row in records:
        print(decrypt(row[0], privkey))
