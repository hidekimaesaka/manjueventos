from flask import Blueprint, jsonify

info_bp = Blueprint('info', __name__)


@info_bp.route('/')
def info():
    return jsonify(about='This is the event service for manjueventos')


def start(app):
    app.register_blueprint(info_bp)
