wsgi_app = 'server:create_app()'
worker_class = 'server.websocket_worker_fix.GeventWebSocketWorker'

access_log_format = '%(t)s %(h)s - %(u)s "%(r)s" %(s)s "%(f)s"'
