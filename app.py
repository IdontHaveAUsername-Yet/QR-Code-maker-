from flask import Flask, render_template, request, send_file
import qrcode
import os

app = Flask(__name__)
QR_FOLDER = "static/qr_codes"

if not os.path.exists(QR_FOLDER):
    os.makedirs(QR_FOLDER)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate_qr', methods=['POST'])
def generate_qr():
    data = request.form.get('qr_data')
    filename = os.path.join(QR_FOLDER, 'qrcode.png')
    
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)

    return send_file(filename, mimetype='image/png')
if not os.path.exists(QR_FOLDER):
    os.makedirs(QR_FOLDER)
    print(f"Folder created at {QR_FOLDER}")
else:
    print(f"Folder already exists at {QR_FOLDER}")


if __name__ == '__main__':
    app.run(debug=True)
