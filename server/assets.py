import os

from flask_assets import Environment, YAMLLoader


def init_assets(server):
    # Create the assets environment with the same debug settings as the server
    server.config['ASSETS_DEBUG'] = server.debug
    Environment(server)

    # Create default asset bundles
    yml_path = os.path.join(os.path.dirname(__file__), 'assets.yml')
    add_assets(server, yml_path)


def add_assets(server, file, prefix=None):
    # Load bundles from the given file
    bundles = YAMLLoader(file).load_bundles()

    for name in bundles:
        # Prefix bundle entries with the given prefix
        if prefix is not None:
            bundles[name].output = prefix + '/' + bundles[name].output
            bundles[name].contents = \
                tuple(map(lambda s: prefix + '/' + s, bundles[name].contents))
        # Register bundle with the webassets environment
        server.jinja_env.assets_environment.register(name, bundles[name])
