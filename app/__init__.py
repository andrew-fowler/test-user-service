from flask import Flask
from flask import json
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)


STATUS_200 = json.dumps({'success': True}), 200, {'ContentType': 'application/json'}
STATUS_404 = json.dumps({'success': False}), 404, {'ContentType': 'application/json'}
STATUS_409 = json.dumps({'success': False}), 409, {'ContentType': 'application/json'}

from app import models, client_endpoints, web_endpoints
