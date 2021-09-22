from flask import Blueprint, make_response, request, jsonify
from flask_expects_json import expects_json
from flask_cors import CORS, cross_origin

from flaskr.services import OwnerServices

bp = Blueprint("owners", __name__, url_prefix="/api/owners")
cors = CORS(bp)
schema = {
    "type": "object",
    "properties": {
        "O_ID": {"type": "number"},
        "O_F_Name": {"type": "string",
                     "minLength": 2,
                     "maxLength": 100,
"pattern": "^[a-zA-Z ]*$"
                     },
        "O_L_Name": {"type": "string",
                     "minLength": 2,
                     "maxLength": 100,
"pattern": "^[a-zA-Z ]*$"
                     },
        "O_Email": {"type": "string",
                    "minLength": 2,
                    "maxLength": 100,
                    "pattern": "^(\w|.|_|-)+[@](\w|_|-|.)+[.]\w{2,3}$"
                    },
        "O_ContactNumber": {"type": "string",
                            "minLength": 2,
                            "maxLength": 100,
                            "pattern": "^[0-9]+$"
                            }
    },
    "required": ["O_F_Name", "O_L_Name", "O_Email", "O_ContactNumber"]
}


@bp.route("/list/<string:order_by>", methods=["GET"])
def list(order_by):
    if request.method == "GET":
        return make_response(jsonify(OwnerServices.getAll(order_by)))


@bp.route("/one/<int:value>", methods=["GET"])
def one(value):
    if request.method == "GET":
        return make_response(jsonify(OwnerServices.getOne(value)))


@bp.route("/create", methods=["POST"])
@expects_json(schema)
def create():
    if request.method == "POST":
        data = request.get_json()
        dic = {"O_F_Name_Value": data["O_F_Name"],
               "O_L_Name_Value": data["O_L_Name"],
               "O_Email_Value": data["O_Email"],
               "O_ContactNumber_Value": data["O_ContactNumber"]}

        return make_response(jsonify(OwnerServices.create(dic=dic)))


@bp.route("/delete/<int:value>", methods=["DELETE"])
def delete(value):
    if request.method == "DELETE":
        return make_response(jsonify(OwnerServices.deleteById(value)))


@bp.route("/update", methods=["POST"])
@expects_json(schema)
def update():
    if request.method == "POST":
        data = request.get_json()
        dic = {"O_ID_Value": data["O_ID"],
               "O_F_Name_Value": data["O_F_Name"],
               "O_L_Name_Value": data["O_L_Name"],
               "O_Email_Value": data["O_Email"],
               "O_ContactNumber_Value": data["O_ContactNumber"]}


        return make_response(jsonify(OwnerServices.updateById(dic=dic)))
