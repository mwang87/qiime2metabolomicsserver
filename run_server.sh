#!/bin/bash
export FLASK_ENV=development
python ./main.py

#gunicorn --daemon -w 4 -b 0.0.0.0:5001 --timeout 3600 main:app
