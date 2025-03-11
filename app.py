from flask import Flask, render_template, request, url_for
import qrcode
import os

app = Flask(__name__)

QR_FOLDER = "static/qr_codes"
os.makedirs(QR_FOLDER, exist_ok=True)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate_qr', methods=['POST'])
def generate_qr():
    url = request.form.get('url')
    if not url:
        return "Error: No URL provided", 400
     
    qr_rel_path = "qr_codes/qr_code.png"
    qr_filename = os.path.join(QR_FOLDER, "qr_code.png")

    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill='black', back_color='white')

    img.save(qr_filename)

    return render_template('index.html', qr_code=qr_rel_path)

if __name__ == '__main__':
    app.run(debug=True)