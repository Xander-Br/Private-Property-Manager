from flask import Blueprint, make_response, request, jsonify
from flask_expects_json import expects_json
from flask_cors import CORS, cross_origin
from flaskr.services import OwnerPropertyServices

bp = Blueprint("owner_properties", __name__, url_prefix="/api/owner_properties")
cors = CORS(bp)


@bp.route("/listBy/<string:O_ID>", methods=["GET"])
def listBy(O_ID):
    if request.method == "GET":
        return make_response(jsonify(OwnerPropertyServices.getAll(O_ID)))

@bp.route("/deleteBy/<int:value>", methods=["DELETE"])
def deleteBy(value):
    if request.method == "DELETE":
        return make_response(jsonify(OwnerPropertyServices.deleteById(value)))

@bp.route("/create", methods=["POST"])
def create():
    if request.method == "POST":
        data = request.get_json()
        dic = {"FK_O_ID_Value": data["FK_O_ID"],
               "FK_P_ID_Value": data["FK_P_ID"]}
        return make_response(jsonify(OwnerPropertyServices.create(dic=dic)))