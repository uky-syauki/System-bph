from flask import Flask, render_template, jsonify
from flask_socketio import SocketIO
from flask_cors import CORS

import cv2 as cv
import numpy as np
import base64
import os

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})
socketio = SocketIO(app)

@app.route('/')
def index():
	return render_template('base.html')


@app.route('/camera')
def camera():
	return render_template('tsocket.html')


@app.route('/api/get-data', methods=['GET','POST'])
def get_data():
	return jsonify(
		{
			'nama':'ahmad syauki',
			'email':'achmad.uky@gmail.com'
		}
		)


@socketio.on('daftar')
def daftar(gambar):
	print('gambar di terima')
	img = gambar.split(',')[1]
	img_bin = img.encode('utf-8')
	img_np = np.frombuffer(base64.b64decode(img_bin), dtype=np.uint8)
	img = cv.imdecode(img_np, cv.IMREAD_COLOR)
	if not os.path.exists('gambar'):
		os.mkdir('gambar')
	cv.imwrite('gambar/t1.png',img)
	print('add gambar')