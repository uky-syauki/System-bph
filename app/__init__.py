from flask import Flask, render_template, jsonify, request
from flask_socketio import SocketIO
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
from datetime import datetime

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


class Calgot(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nama_panggilan = db.Column(db.String(30))
    nama_lengkap = db.Column(db.String(100))
    email = db.Column(db.String(120))
    nomor_wa = db.Column(db.String(15))
    asal_kampus = db.Column(db.String(120))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    def __repr__(self):
        return f'<Calgot: {self.nama_panggilan}>'


@app.route('/')
@app.route('/index')
def index():
    return "Bismillah"


@app.route('/api/mendaftar', methods=['POST','GET'])
def mendaftar():
    data = request.form
    print("Menerima", data)
    calgot = Calgot(nama_panggilan=data['nama_panggilan'],nama_lengkap=data['nama_lengkap'], email=data['email'],nomor_wa=data['nomorWA'], asal_kampus=data['asalKampus'])
    db.session.add(calgot)
    db.session.commit()
    print("Calgot berhasil di daftar", data['nama_panggilan'])



    # return redirect('https://google.com')
    return jsonify({'status':'Sukses', 'pesan':'Data Diterima'})
