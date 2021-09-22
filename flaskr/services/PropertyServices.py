import json

import pymysql
import sys
from flaskr.database.db import db

invalid = 403
ok = 200

TABLE_NAME = "t_property"
GET_ALL = """SELECT * FROM t_property ORDER BY P_ID """

GET_ONE = """SELECT * FROM t_property WHERE P_ID = %(value)s"""

CREATE = """INSERT INTO t_property (P_ID, P_Name, P_Price, P_Description, P_Type, P_Construction_Year) VALUES (NULL, %(P_Name_Value)s, %(P_Price_Value)s, %(P_Description_Value)s ,%(P_Type_Value)s, %(P_Construction_Year_Value)s);"""

UPDATE = """UPDATE t_property SET P_Name = %(P_Name_Value)s, P_Price = %(P_Price_Value)s, P_Description = %(P_Description_Value)s, P_Type = %(P_Type_Value)s,P_Construction_Year = %(P_Construction_Year_Value)s WHERE t_property.P_ID = %(P_ID_Value)s;"""

DELETE = """DELETE FROM t_property WHERE P_ID = %(value)s"""
DELETE_INTERMEDIATE = """DELETE FROM t_owner_property WHERE FK_P_ID = %(value)s"""


def getAll(order_by):
    try:
        try:
            db().conn.ping(False)
        except Exception as err:
            print(f"Error in Property Services - 'getAll()'\nerror:{err}")
            return "{error:" + err + "'}"

        with db().conn.cursor() as cursor:
            if order_by == "ASC":
                print(GET_ALL + " ASC")
                cursor.execute(GET_ALL + " ASC")
            else:
                print(GET_ALL + " DESC")
                cursor.execute(GET_ALL + " DESC")

            data = cursor.fetchall()

            return data
    except Exception as err:
        print(f"Error in Property Services - 'all()'\nerror:{err}")
        return f"error: {err}"


def getOne(value):
    try:
        try:
            db().conn.ping(False)
        except Exception as err:
            print(f"Error in Property Services - 'getOne()'\nerror:{err}")
            return "{error:" + err + "'}"

        with db().conn.cursor() as cursor:
            value = {"value": value}
            cursor.execute(GET_ONE, value)

            data = cursor.fetchone()

            return data

    except Exception as err:
        print(f"Error in Property Services - getOne()'\nerror:{err}")
        return err
    return "test"


def create(dic):
    try:
        try:
            db().conn.ping(False)
        except Exception as err:
            print(f"Error in Property Services - 'getOne()'\nerror:{error}")
            return "{error:" + err + "'}", invalid

        with db() as cursor:
            cursor.execute(CREATE, dic)
            return "Successfully inserted", ok

    except pymysql.err.IntegrityError as err:
        code, msg = err.args
        err_dic = {"error": {
            "code": code,
            "msg": msg
        }}
        print(f"Error in Property Services - 'create()'\nerror:{dic}")
        return err_dic

    except (pymysql.err.OperationalError,
            pymysql.ProgrammingError,
            pymysql.InternalError,
            TypeError) as err:
        code, msg = err.args
        err_dic = {"error": {
            "code": code,
            "msg": msg
        }}
        print(f"Error in Property Services - 'create()'\nerror:{dic}")
        return err_dic


def deleteById(value):
    try:
        try:
            db().conn.ping(False)
        except Exception as err:
            print(f"Error in Property Services - 'deleteById()'\nerror:{error}")
            return "{error:" + err + "'}"

        with db() as cursor:
            dic = {"value": value}
            print(DELETE_INTERMEDIATE, dic)
            print(DELETE, dic)
            cursor.execute(DELETE_INTERMEDIATE, dic)
            cursor.execute(DELETE, dic)
        return "Successfully deleted", ok

    except KeyError:
        code, msg = err.args
        err_dic = {"error": {
            "code": {
                "info_0": sys.exc_info()[0],
                "info_1": sys.exc_info()[1],
                "info_2": sys.exc_info()[2]
            },
            "msg": "Key Error in deleteById()"
        }}
        return err_dic

    except ValueError:
        err_dic = {"error": {
            "code": {
                "info_0": sys.exc_info()[0],
                "info_1": sys.exc_info()[1],
            },
            "msg": "Value Error in deleteById()"
        }}
        return err_dic

    except (pymysql.err.OperationalError,
            pymysql.ProgrammingError,
            pymysql.InternalError,
            pymysql.err.IntegrityError,
            TypeError) as err:
        code, msg = err.args
        err_dic = {"error": {
            "code": code,
            "msg": msg
        }}
        print(f"Error in Property Services - 'deleteById()'\nerror:{dic}")
        return err_dic

    return "Success"


def updateById(dic):
    try:
        try:
            db().conn.ping(False)
        except Exception as err:
            print(f"Error in Owner Services - 'updateById()'\nerror:{error}")
            return "{error:" + err + "'}"

        with db() as cursor:
            print(UPDATE, dic)
            cursor.execute(UPDATE, dic)
        return "Successfully edited", ok

    except KeyError:


        err_dic = {"error": {
            "code": {
                "info_0": sys.exc_info()[0],
                "info_1": sys.exc_info()[1],
                "info_2": sys.exc_info()[2]
            },
            "msg": "Key Error in updateById()"
        }}
        print(err_dic)
        return err_dic

    except ValueError:
        err_dic = {"error": {
            "code": {
                "info_0": sys.exc_info()[0],
                "info_1": sys.exc_info()[1],
            },
            "msg": "Value Error in updateById()"
        }}
        return err_dic

    except (pymysql.err.OperationalError,
            pymysql.ProgrammingError,
            pymysql.InternalError,
            pymysql.err.IntegrityError,
            TypeError) as err:
        code, msg = err.args
        err_dic = {"error": {
            "code": code,
            "msg": msg
        }}
        print(f"Error in Owner Services - 'updateById()'\nerror:{dic}")
        return err_dic
    return "Success"
