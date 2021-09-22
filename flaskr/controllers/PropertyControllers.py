from flask import Blueprint, make_response, request, jsonify
from flask_expects_json import expects_json

from flaskr.services import PropertyServices

bp = Blueprint("property", __name__, url_prefix="/api/properties")

schema = {
    "type": "object",
    "properties": {
        "P_ID": {"type": "number"},
        "P_Name": {"type": "string",
                   "minLength": 2,
                   "maxLength": 100
                   },
        "P_Price": {"type": ["string", "number"]},
        "P_Description": {"type": "string",
                          "minLength": 2,
                          "maxLength": 100,
                          },
        "P_Type": {"type": "string",
                   "minLength": 2,
                   "maxLength": 100,
                   },
        "P_Construction_Year": {"type": "string"}
    },
    "required": ["P_Name", "P_Price", "P_Description", "P_Type", "P_Construction_Year"]
}


@bp.route("/list/<string:order_by>", methods=["GET"])
def list(order_by):
    if request.method == "GET":
        return make_response(jsonify(PropertyServices.getAll(order_by)))


@bp.route("/one/<int:value>", methods=["GET"])
def one(value):
    if request.method == "GET":
        return make_response(jsonify(PropertyServices.getOne(value)))


@bp.route("/create", methods=["POST"])
@expects_json(schema)
def create():
    if request.method == "POST":
        data = request.get_json()
        dic = {"P_Name_Value": data["P_Name"],
               "P_Price_Value": data["P_Price"],
               "P_Description_Value": data["P_Description"],
               "P_Type_Value": data["P_Type"],
               "P_Construction_Year_Value": data["P_Construction_Year"]
               }

        return make_response(jsonify(PropertyServices.create(dic=dic)))


@bp.route("/delete/<int:value>", methods=["DELETE"])
def delete(value):
    if request.method == "DELETE":
        return make_response(jsonify(PropertyServices.deleteById(value)))


@bp.route("/update", methods=["POST"])
@expects_json(schema)
def update():
    if request.method == "POST":
        data = request.get_json()
        print(data)
        dic = {"P_ID_Value": data["P_ID"],
         "P_Name_Value": data["P_Name"],
         "P_Price_Value": data["P_Price"],
         "P_Description_Value": data["P_Description"],
         "P_Type_Value": data["P_Type"],
         "P_Construction_Year_Value": data["P_Construction_Year"]
         }

        return make_response(jsonify(PropertyServices.updateById(dic)))
