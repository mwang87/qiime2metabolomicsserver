#!/bin/bash

gunicorn --daemon -w 4 -b 0.0.0.0:5000 --timeout 3600 main:app
