import pymysql
from flask import flash
from pymysql.constants import CLIENT

from flaskr import HOST_MYSQL
from flaskr import NAME_BD_MYSQL
from flaskr import PASS_MYSQL
from flaskr import PORT_MYSQL
from flaskr import USER_MYSQL

class db():
    def __init__(self):
        self.conn = None
        try:
            self.conn = pymysql.connect(host=HOST_MYSQL,
                                                user=USER_MYSQL,
                                                password=PASS_MYSQL,
                                                db=NAME_BD_MYSQL,
                                                port=PORT_MYSQL,
                                                client_flag=CLIENT.MULTI_STATEMENTS,
                                                cursorclass=pymysql.cursors.DictCursor,
                                                autocommit=False)
        except (Exception, ConnectionRefusedError, pymysql.err.OperationalError, pymysql.err.DatabaseError) as e:
            print("Error instanciating db")
            print(e)


    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("exc_val ", exc_type, exc_val, exc_tb)

        if exc_val is None:
            self.conn.commit()
        else:
            self.conn.rollback()

        self.conn.close()

    def execute(self,sql,params = None):
        return self.conn.cursor().execute(sql, params or ())

    def fetchall(self):
        return self.conn.cursor().fetchall()