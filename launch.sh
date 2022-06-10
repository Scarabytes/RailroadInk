#!/bin/bash

./venv/bin/gunicorn -b 127.0.0.1:5000 -c gunicorn.conf.py
