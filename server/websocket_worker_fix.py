from geventwebsocket.handler import WebSocketHandler
from gunicorn.workers.ggevent import GeventPyWSGIWorker, PyWSGIHandler


# Fix GeventWebSocketWorker not outputting access logs
# (https://github.com/jgelens/gevent-websocket/pull/9)
class GeventSocketHandler(PyWSGIHandler, WebSocketHandler):
    pass


class GeventWebSocketWorker(GeventPyWSGIWorker):
    wsgi_handler = GeventSocketHandler
