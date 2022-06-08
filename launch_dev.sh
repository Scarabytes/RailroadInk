#!/bin/bash

export FLASK_APP=server
export FLASK_ENV=development
export FLASK_DEBUG=1

./venv/bin/python -m flask run
