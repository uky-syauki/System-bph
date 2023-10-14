from app import app, db
from flask import request, redirect, jsonify
from app.models import Calgot

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

