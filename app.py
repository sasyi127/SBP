# coding=utf-8
import os
import numpy as np

# Keras
from keras.models import load_model
from keras.utils import img_to_array
from keras.utils import load_img

# Flask utils
from flask import Flask, request, render_template
from werkzeug.utils import secure_filename
# from gevent.pywsgi import WSGIServer

# Define a flask app
app = Flask(__name__)

# Model saved with Keras model.save()
MODEL_PATH = 'models/SBPFixed_Model.h5'

# Load your trained model
model = load_model(MODEL_PATH)


def model_predict(img_path, model):
    img = load_img(img_path, target_size=(150, 150))

    # Preprocessing the image
    x = img_to_array(img)
    x = np.expand_dims(x, axis=0)

    # Be careful how your trained model deals with the input
    # otherwise, it won't make correct prediction!

    preds = model.predict(x)
    preds = np.argmax(preds, axis=1)
    if preds == 0:
        preds = "Ini adalah Cacar Air"
    elif preds == 1:
        preds = "Ini adalah Herpes"
    elif preds == 2:
        preds = "ini adalah Impetigo"
    elif preds == 3:
        preds = "Ini adalah Kurap"
    elif preds == 4:
        preds = "Ini adalah Kutil"
    elif preds == 5:
        preds = "Ini adalah Melanoma"
    elif preds == 6:
        preds = "Ini adalah Psoriasis"
    elif preds == 7:
        preds = "Ini adalah Vitiligo"

    return preds


def solusi_predict(img_path, model):
    img = load_img(img_path, target_size=(150, 150))

    # Preprocessing the image
    x = img_to_array(img)
    x = np.expand_dims(x, axis=0)

    # Be careful how your trained model deals with the input
    # otherwise, it won't make correct prediction!

    preds = model.predict(x)
    preds = np.argmax(preds, axis=1)
    if preds == 0:
        preds = """
        <h5>Cara Mengatasi Cacar Air</h5>
        <ul>
            <li>Konsumsi obat penghilang rasa sakit untuk membantu mengurangi demam tinggi dan rasa sakit ketika seseorang menderita cacar air.</li>
            <li>Minum banyak cairan, lebih disukai air, untuk mencegah dehidrasi, yang dapat menjadi komplikasi cacar air.</li>
            <li>Hindari makanan asin atau pedas. Jika mengunyah terasa sakit, sup bisa menjadi pilihan yang baik, asalkan tidak terlalu panas.</li>
            <li>Untuk menghindari gatal bisa menjadi parah, dengan memakai salep, jangan menggaruk luka dan menjaga kuku tetap bersih. Terakhir gunakan pakaian longgar. </li>
            <li>Dokter mungkin meresepkan obat antivirus selama kehamilan, untuk orang dewasa yang mendapatkan diagnosis dini, untuk bayi baru lahir, dan bagi mereka yang memiliki sistem kekebalan yang lemah. </li>
        </ul>
        """
    elif preds == 1:
        preds = """
        <h5>Cara Mengatasi Herpes</h5>
        <ul>
            <li>Kompres menggunakan air hangat atau dingin pada bagian yang sering muncul herpes untuk meredakan rasa sakit</li>
            <li>Aplikasikan tumbukan halus bawang putih dan minyak zaitun pada bagian tubuh yang terdampak virus herpes tiga kali sehari </li>
            <li>Oleskan Cuka Apel ke bagian tubuh yang terdampak virus. Cuka apel memiliki komponen anti inflamasi yang bisa membuat luka cepat kering</li>
            <li>Mengonsumsi suplemen seperti yogurt, vitamin B dan zinc dengan takaran 30 mg per hari untuk mengatasi penyebaran virus </li>
            <li>Mengatur pola makan yang baik untuk mencegah penurunan daya tahan tubuh</li>
            <li>Gunakan Obat-obatan yang mudah ditemukan di apotek terdekat. Seperti (Betason N Cream, Valtrex Tablet, Zovirax Cream, Acyclovir Cream, Zoter Cream, Virugon Natural Cream)</li>
        </ul>
        """
    elif preds == 2:
        preds = """
        <h5>Cara Mengatasi Impetigo</h5>
        <ul>
            <li>Merendam luka dengan menggunakan air hangat</li>
            <li>Gunakan salep atau krim antibiotik</li>
            <li>Apabila impetigo semakin parah dan mulai menyebar ke bagian tubuh lainnya, meminum obat seperti clindamycin atau obat antibiotik golongan sefalosporin</li>
        </ul>
        """
    elif preds == 3:
        preds = """
        <h5>Cara Mengatasi Kurap</h5>
        <ul>
            <li>Cuci sprei dan pakaian setiap hari selama infeksi untuk membantu membunuh jamur-jamur yang ada di lingkungan Anda</li>
            <li>Keringkan area tubuh secara menyeluruh setelah mandi</li>
            <li>Gunakan pakaian longgar di daerah yang terkena kurap</li>
            <li>Obati semua area yang terinfeksi dengan produk yang mengandung clotrimazole, miconazole, terbinafine, atau bahan terkait lainnya</li>
        </ul>
        """
    elif preds == 4:
        preds = """
        <h5>Cara Mengatasi Kutil</h5>
        <ul>
            <li>Perawatan dengan nitrogen cair/cryotherapy</li>
            <li>Operasi pembedahan</li>
            <li>Perawatan laser</li>
        </ul>
        """
    elif preds == 5:
        preds = """
        <h5>Cara Mengatasi Melanoma</h5>
        <ul>
            <li>Operasi atau pembedahan jadi pengobatan</li>
            <li>Terapi radiasi</li>
            <li>Kemoterapi</li>
        </ul>
        """
    elif preds == 6:
        preds = """
        <h5>Cara Mengatasi Psoriasis</h5>
        <ul>
            <li>Mengenal dan menjauhi faktor pemicu gejala psoriasis</li>
            <li>Membatasi waktu mandi</li>
            <li>Mengoleskan pelembap pada kulit</li>
            <li>Menjalani pola makan sehat</li>
            <li>Mengelola stres dengan baik</li>
            <li>Menggunakan bahan alami</li>
        </ul>
        """
    elif preds == 7:
        preds = """
        <h5>Cara Mengatasi Vitiligo</h5>
        <ul>
            <li>Obat yang mengontrol peradangan.</li>
            <li>Pengobatan yang mempengaruhi sistem kekebalan.</li>
            <li>Terapi cahaya seperti Fototerapi dengan ultraviolet B pita sempit (UVB)</li>
            <li>Operasi Cangkok kulit.</li>
            <li>Transplantasi suspensi seluler.</li>
        </ul>
        """

    return preds


@app.route('/', methods=['GET'])
def index():
    # Main page
    return render_template('index.html')


@app.route('/predict', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # Get the file from post request
        f = request.files['file']

        # Save the file to ./uploads
        basepath = os.path.dirname(__file__)
        file_path = os.path.join(
            basepath, 'images', secure_filename(f.filename))
        f.save(file_path)

        # Make prediction
        preds = model_predict(file_path, model)
        result = preds
        return result
    return None


@app.route('/solusi', methods=['GET', 'POST'])
def solusi():
    if request.method == 'POST':
        # Get the file from post request
        f = request.files['file']

        # Save the file to ./uploads
        basepath = os.path.dirname(__file__)
        file_path = os.path.join(
            basepath, 'images', secure_filename(f.filename))
        f.save(file_path)

        # Make prediction
        preds = solusi_predict(file_path, model)
        result = preds
        return result
    return None


if __name__ == '__main__':
    app.run()
