from . import create_app

# Minimal script to make the server package executable
# Launching via flask is preferred
server = create_app()
server.run()
