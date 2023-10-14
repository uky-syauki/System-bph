from flask import Flask, render_template, jsonify
from flask_socketio import SocketIO
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

import cv2 as cv
import numpy as np
import base64
import os

app = Flask(__name__)
app.config.from_object(Config)
CORS(app, resources={r"/*": {"origins": "*"}})
socketio = SocketIO(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
# cors = CORS(app, resources={r"/socket.io/*": {"origins": "*"}})


from app import routes, models
