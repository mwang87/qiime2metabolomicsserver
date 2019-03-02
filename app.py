# app.py
import os

from flask import Flask

APP_ROOT = os.path.dirname(os.path.realpath(__file__))

class CustomFlask(Flask):
  jinja_options = Flask.jinja_options.copy()
  jinja_options.update(dict(
    block_start_string='(%',
    block_end_string='%)',
    variable_start_string='((',
    variable_end_string='))',
    comment_start_string='(#',
    comment_end_string='#)',
  ))

app = CustomFlask(__name__)
app.config.from_object(__name__)
app.config['UPLOAD_FOLDER'] = './tempuploads'

try:
    os.mkdir(app.config['UPLOAD_FOLDER'])
except:
    print("Cannot Create", app.config['UPLOAD_FOLDER'])
