import logging
import pymysql

from flask import json, send_from_directory, render_template
from flask_cors import CORS
from werkzeug.exceptions import HTTPException

from flaskr import create_app
from flaskr.database.db import db
from flaskr.database import dbTools


app = create_app()
CORS(app, resources={r"/*": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'application/json'

logging.getLogger('flask_cors').level = logging.DEBUG


@app.route("/api/import")
def importDump():
    try:
        objet_dumpbd = dbTools.Toolsbd().load_dump_sql_bd_init()
    except Exception as erreur_load_dump_sql:
        print(f"Initialisation de la BD Impossible ! (voir DUMP ou .env) "
              f"{erreur_load_dump_sql.args[0]} , "
              f"{erreur_load_dump_sql}")
    return "imported"


@app.errorhandler(Exception)
def handle_exception(e):
    # pass through HTTP errors
    if isinstance(e, HTTPException):
        return e


@app.errorhandler(HTTPException)
def handle_exception(e):
    """Return JSON instead of HTML for HTTP errors."""
    # start with the correct headers and status code from the error
    response = e.get_response()
    # replace the body with JSON
    response.data = json.dumps(
        {"error": {
            "code": e.code,
            "name": e.name,
            "description": e.description,
        }
        }
    )
    response.content_type = "application/json"
    return response




if __name__ == "__main__":
    app.run()
