import os

from flask import Blueprint, render_template

from assets import add_assets


# RailroadInk Blueprint
bp = Blueprint('railroadink', __name__,
               url_prefix='/railroadink',
               template_folder='templates',
               static_folder='static')


# Initialize this blueprint and register it with the given flask server
def init(server):
    # Add local assets
    yml_path = os.path.join(os.path.dirname(__file__), 'assets.yml')
    add_assets(server, yml_path, bp.name)

    # Register blueprint with server
    server.register_blueprint(bp)


@bp.route('/')
def index():
    return render_template('game.html')
