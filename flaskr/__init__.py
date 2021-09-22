
import os
import environs
from environs import Env
from flask import Flask, send_from_directory, url_for, render_template


HOST_MYSQL = None
USER_MYSQL = None
PASS_MYSQL = None
PORT_MYSQL = None
NAME_BD_MYSQL = None
NAME_FILE_DUMP_SQL_BD = None

ADRESSE_SRV_FLASK = None
DEBUG_FLASK = None
PORT_FLASK = None
SECRET_KEY_FLASK = None
WTF_CSRF_ENABLED = True




try:
    env = Env()
    env.read_env()
    
    HOST_MYSQL = env("HOST_MYSQL")
    USER_MYSQL = env("USER_MYSQL")
    PASS_MYSQL = env("PASS_MYSQL")
    PORT_MYSQL = int(env("PORT_MYSQL"))  # Pour la connection à la BD le port doit être une valeur numérique INT
    NAME_BD_MYSQL = env("NAME_BD_MYSQL")
    NAME_FILE_DUMP_SQL_BD = env("NAME_FILE_DUMP_SQL_BD")

    ADRESSE_SRV_FLASK = env("ADRESSE_SRV_FLASK")
    DEBUG_FLASK = env("DEBUG_FLASK")
    PORT_FLASK = env("PORT_FLASK")
    SECRET_KEY_FLASK = env("SECRET_KEY_FLASK")

except environs.EnvError as e:
    print(f"Error with env var")



def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY= SECRET_KEY_FLASK,
        DEBUG_FLASK= DEBUG_FLASK,
        PORT_FLASK= PORT_FLASK,
        SECRET_KEY_FLASK= SECRET_KEY_FLASK,
        template_folder="templates",
        static_url_path="templates"
    )



    @app.errorhandler(500)
    def server_error(e):
        return 'An internal error occurred [main.py] %s' % e, 500

    @app.route('/<path:path>', methods=['GET'])
    def static_proxy(path):
        return send_from_directory('templates', path)

    @app.route('/')
    def root():
        return send_from_directory('templates', 'index.html')


    from flaskr.controllers import OwnerControllers
    app.register_blueprint(OwnerControllers.bp)

    from flaskr.controllers import PropertyControllers
    app.register_blueprint(PropertyControllers.bp)

    from flaskr.controllers import  OwnerPropertyController
    app.register_blueprint(OwnerPropertyController.bp)

    return app