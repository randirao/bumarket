from typing import Optional

import pymysql
from pymysql import Connection
from pymysql.cursors import Cursor

con: Optional[Connection] = None
cur: Optional[Cursor] = None

def get_connection():
    return pymysql.connect(
        host='127.0.0.1',
        user='root',
        port=3306,
        password='q1w2e3',
        database='bumaket',
        cursorclass=pymysql.cursors.DictCursor
    )

con = get_connection()
cur = con.cursor()