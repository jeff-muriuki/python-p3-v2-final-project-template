import sqlite3

CONN = sqlite3.connect('chainstore.db')
CURSOR = CONN.cursor()
