import os
import logging

from flask import Flask, render_template
from werkzeug.debug import DebuggedApplication

from . import railroadink
from . import assets
from . import sockets


def create_app(test_config=None):
    # Create Flask server
    app = Flask(__name__,
                instance_relative_config=True)

    # Link to gunicorn's logger
    gunicorn_logger = logging.getLogger('gunicorn.error')
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)

    # Log application's root path
    app.logger.debug('Root Path: %s', app.root_path)

    # Fill in (development) config defaults
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

    # Register all components
    assets.init_assets(app)
    sockets.init_sockets(app)
    railroadink.init(app)

    # Dummy index page
    @app.route('/')
    def index():
        return render_template('base.html')

    io = sockets.get_sockets(app)

    # Dummy websocket event handler
    @io.on('message')
    def msg(data):
        app.logger.info('received: ' + data)
        io.send('Hello Client.')

    # Enable debugging server if needed
    if app.debug:
        app.wsgi_app = DebuggedApplication(app.wsgi_app, evalex=True)

        @app.route('/debug')
        def open_debugger():
            raise

    return app
