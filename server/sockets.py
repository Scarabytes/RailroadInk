from flask_socketio import SocketIO


def init_sockets(server):
    SocketIO(server)


def get_sockets(server):
    return server.extensions['socketio']
