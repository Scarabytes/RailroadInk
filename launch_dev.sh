#!/bin/bash

./venv/bin/gunicorn \
    --reload --access-logfile - --log-level debug -e FLASK_DEBUG=1 \
    -b 127.0.0.1:5000 -c gunicorn.conf.py
