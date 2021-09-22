import pymysql

from flaskr.database.db import db

invalid = 403
ok = 200

TABLE_NAME = "t_owner_property"
GET_ONE = """SELECT 
    breuil_alexandre_info1b_private_property_manager_104.t_property.P_ID, 
    breuil_alexandre_info1b_private_property_manager_104.t_property.P_Name, 
    breuil_alexandre_info1b_private_property_manager_104.t_property.P_Price, 
    breuil_alexandre_info1b_private_property_manager_104.t_property.P_Description, 
    breuil_alexandre_info1b_private_property_manager_104.t_property.P_Type, 
    breuil_alexandre_info1b_private_property_manager_104.t_property.P_Construction_Year 
FROM 
    breuil_alexandre_info1b_private_property_manager_104.t_owner_property 
INNER JOIN 
    breuil_alexandre_info1b_private_property_manager_104.t_property 
ON 
    ( 
        breuil_alexandre_info1b_private_property_manager_104.t_owner_property.FK_P_ID = 
        breuil_alexandre_info1b_private_property_manager_104.t_property.P_ID) WHERE FK_O_ID = %(value)s"""

CREATE = """INSERT INTO t_owner_property (OP_ID, FK_O_ID, FK_P_ID) VALUES (NULL, %(FK_O_ID_Value)s, %(FK_P_ID_Value)s);"""
DELETE_INTERMEDIATE = """DELETE FROM t_owner_property WHERE FK_P_ID = %(value)s"""

def getAll(value):
    try:
        try:
            db().conn.ping(False)
        except Exception as err:
            print(f"Error in Owner Services - 'getOne()'\nerror:{err}")
            return "{error:" + err + "'}"

        with db().conn.cursor() as cursor:
            value = {"value": value}
            cursor.execute(GET_ONE, value)

            data = cursor.fetchall()

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
            print(f"Error in Property Services - 'deleteById()'\nerror:{error}")
            return "{error:" + err + "'}"

        with db() as cursor:
            dic = {"value": value}
            print(DELETE_INTERMEDIATE, dic)

            cursor.execute(DELETE_INTERMEDIATE, dic)
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

