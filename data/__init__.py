from typing import Optional

import pymysql
from pymysql import Connection
from pymysql.cursors import Cursor

con: Optional[Connection] = None
cur: Optional[Cursor] = None

def get_connection():
    return pymysql.connect(
        host='localhost',
        user='root',
        port=3306,
        password='todos',
        database='bumaket',
        cursorclass=pymysql.cursors.DictCursor
    )

con = get_connection()
cur = con.cursor()