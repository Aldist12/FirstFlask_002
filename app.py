from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Route untuk halaman utama dengan method GET dan POST
@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    
    if request.method == 'POST':
        # Parsing parameter dari form
        nama = request.form.get('nama')
        email = request.form.get('email')
        pesan = request.form.get('pesan')
        
        # Proses data (contoh sederhana)
        result = {
            'nama': nama,
            'email': email,
            'pesan': pesan,
            'status': 'Data berhasil diterima!'
        }
    
    return render_template('index.html', result=result)

# Route tambahan untuk demo POST endpoint terpisah
@app.route('/submit', methods=['POST'])
def submit_data():
    # Parsing parameter dari form
    data = {
        'nama': request.form.get('nama'),
        'email': request.form.get('email'),
        'pesan': request.form.get('pesan')
    }
    
    # Redirect kembali ke halaman utama dengan parameter
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)