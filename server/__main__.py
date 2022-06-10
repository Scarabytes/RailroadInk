from . import create_app
from . import sockets

# Minimal script to make the server package executable
# Launching via gunicorn is preferred
server = create_app()
sockets.get_sockets(server).run(server)
