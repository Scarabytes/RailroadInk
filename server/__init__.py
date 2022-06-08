import os

from flask import Flask, render_template

import railroadink
from . import assets


def create_app(test_config=None):
    # Create Flask server
    app = Flask(__name__,
                instance_relative_config=True)
    print(' * Root Path:', app.root_path)

    # Fill in (development) defaults
    app.config.from_mapping(
        SECRET_KEY='dev',
    )

    # Ensure the instance folder and config file exists
    if not os.path.exists(app.instance_path):
        os.makedirs(app.instance_path)
    if not os.path.exists(app.instance_path + '/config.py'):
        os.mknod(app.instance_path + '/config.py')

    if test_config is not None:
        # Load the test config if passed in
        app.config.from_mapping(test_config)
    else:
        # Load the instance config when not testing
        app.config.from_pyfile('config.py')

    # Dummy index page
    @app.route('/')
    def index():
        return render_template('base.html')

    # Register all components
    assets.init_assets(app)
    railroadink.init(app)

    return app
