import pymysql

from flaskr.database.db import db

invalid = 403
ok = 200

TABLE_NAME = "t_owner"
GET_ALL = """SELECT * FROM t_owner ORDER BY O_ID"""
GET_ONE = """SELECT * FROM t_owner WHERE O_ID = %(value)s"""
CREATE = """INSERT INTO t_owner (O_ID, O_F_Name, O_L_Name, O_Email, O_ContactNumber) VALUES (NULL, %(O_F_Name_Value)s, %(O_L_Name_Value)s, %(O_Email_Value)s, %(O_ContactNumber_Value)s);"""
UPDATE = """UPDATE t_owner SET O_F_Name = %(O_F_Name_Value)s, O_L_Name = %(O_L_Name_Value)s, O_Email = %(O_Email_Value)s, O_ContactNumber = %(O_ContactNumber_Value)s WHERE t_owner.O_ID = %(O_ID_Value)s;"""

DELETE = """DELETE FROM t_owner WHERE t_owner.O_ID = %(value)s"""
DELETE_INTERMEDIATE = """DELETE FROM t_owner_property WHERE t_owner_property.FK_O_ID = %(value)s"""


def getAll(order_by):
    try:
        try:
            db().conn.ping(False)
        except Exception as err:
            print(f"Error in Owner Services - 'getAll()'\nerror:{err}")
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
        print(f"Error in Owner Services - 'all()'\nerror:{err}")
        return f"error: {err}"


def getOne(value):
    try:
        try:
            db().conn.ping(False)
        except Exception as err:
            print(f"Error in Owner Services - 'getOne()'\nerror:{err}")
            return "{error:" + err + "'}"

        with db().conn.cursor() as cursor:
            value = {"value": value}
            cursor.execute(GET_ONE, value)

            data = cursor.fetchone()

            return data
    except Exception as err:
        print(f"Error in Owner Services - getOne()'\nerror:{err}")
        return err
    return "test"


def create(dic):
    try:
        try:
            db().conn.ping(False)
        except Exception as err:
            print(f"Error in Owner Services - 'getOne()'\nerror:{error}")
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
        print(f"Error in Owner Services - 'create()'\nerror:{dic}")
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
        print(f"Error in Owner Services - 'create()'\nerror:{dic}")
        return err_dic


def deleteById(value):
    try:
        try:
            db().conn.ping(False)
        except Exception as err:
            print(f"Error in Owner Services - 'deleteById()'\nerror:{error}")
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
        print(f"Error in Owner Services - 'deleteById()'\nerror:{dic}")
        return err_dic

    return "Success"


def updateById(dic):
    print("TEst")
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

        code, msg = err.args

        err_dic = {"error": {
            "code": {
                "info_0": sys.exc_info()[0],
                "info_1": sys.exc_info()[1],
                "info_2": sys.exc_info()[2]
            },
            "msg": "Key Error in updateById()"
        }}
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
