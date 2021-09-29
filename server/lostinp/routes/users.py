from flask import Blueprint, jsonify


mod = Blueprint("users", __name__, url_prefix="/users")


@mod.route("/login")
def login():
    return jsonify({})


@mod.route("/logout")
def logout():
    return jsonify({})
