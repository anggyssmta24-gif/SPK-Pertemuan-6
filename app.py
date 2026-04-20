from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'spk_pkl'

mysql = MySQL(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/tempat_pkl', methods=['GET', 'POST'])
def tempat_pkl():
    if request.method == 'POST':
        nama_pkl = request.form['nama_pkl']
        lokasi_pkl = request.form['lokasi_pkl']
        jarak = request.form['jarak']
        fasilitas = request.form['fasilitas']
        reputasi = request.form['reputasi']

        cur = mysql.connection.cursor()
        cur.execute("""
            INSERT INTO tempat_pkl (nama_pkl, lokasi_pkl, jarak, fasilitas, reputasi)
            VALUES (%s, %s, %s, %s, %s)
        """, (nama_pkl, lokasi_pkl, jarak, fasilitas, reputasi))
        mysql.connection.commit()
        cur.close()

        return redirect('/tempat_pkl')

    return render_template('tempat_pkl.html')

@app.route('/list_tempat_pkl')
def list_tempat_pkl():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM tempat_pkl")
    data = cur.fetchall()
    cur.close()

    return render_template('list_tempat_pkl.html', data=data)

@app.route('/edit_tempat_pkl/<int:id>', methods=['GET', 'POST'])
def edit_tempat_pkl(id):
    cur = mysql.connection.cursor()

    if request.method == 'POST':
        nama_pkl = request.form['nama_pkl']
        lokasi_pkl = request.form['lokasi_pkl']
        jarak = request.form['jarak']
        fasilitas = request.form['fasilitas']
        reputasi = request.form['reputasi']

        cur.execute("""
            UPDATE tempat_pkl
            SET nama_pkl=%s, lokasi_pkl=%s, jarak=%s, fasilitas=%s, reputasi=%s
            WHERE id_pkl=%s
        """, (nama_pkl, lokasi_pkl, jarak, fasilitas, reputasi, id))

        mysql.connection.commit()
        cur.close()

        return redirect('/list_tempat_pkl')

    cur.execute("SELECT * FROM tempat_pkl WHERE id_pkl = %s", (id,))
    data = cur.fetchone()
    cur.close()

    return render_template('edit_tempat_pkl.html', data=data)

@app.route('/hapus_tempat_pkl/<int:id>')
def hapus_tempat_pkl(id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM tempat_pkl WHERE id_pkl = %s", (id,))
    mysql.connection.commit()
    cur.close()

    return redirect('/list_tempat_pkl')

@app.route('/hasil')
def hasil():
    cur = mysql.connection.cursor()

    cur.execute("SELECT * FROM tempat_pkl")
    data = cur.fetchall()

    hasil_perhitungan = []

    for row in data:
        id_pkl = row[0]
        nama_pkl = row[1]
        lokasi = row[2]
        jarak = row[3]
        fasilitas = row[4]
        reputasi = row[5]

        # Konversi jarak
        if jarak == 'Dekat':
            nilai_jarak = 3
        elif jarak == 'Sedang':
            nilai_jarak = 2
        else:
            nilai_jarak = 1

        # Konversi fasilitas
        if fasilitas == 'Lengkap':
            nilai_fasilitas = 3
        elif fasilitas == 'Cukup':
            nilai_fasilitas = 2
        else:
            nilai_fasilitas = 1

        # Konversi reputasi
        if reputasi == 'Sangat Baik':
            nilai_reputasi = 3
        elif reputasi == 'Baik':
            nilai_reputasi = 2
        else:
            nilai_reputasi = 1

        # Bobot
        bobot_jarak = 0.20
        bobot_fasilitas = 0.30
        bobot_reputasi = 0.50

        # Perhitungan SAW
        nilai_akhir = (
            (nilai_jarak / 3) * bobot_jarak +
            (nilai_fasilitas / 3) * bobot_fasilitas +
            (nilai_reputasi / 3) * bobot_reputasi
        )

        hasil_perhitungan.append({
            'nama_pkl': nama_pkl,
            'lokasi': lokasi,
            'nilai': round(nilai_akhir, 3)
        })

    hasil_perhitungan = sorted(
        hasil_perhitungan,
        key=lambda x: x['nilai'],
        reverse=True
    )

    cur.close()

    return render_template('hasil.html', hasil=hasil_perhitungan)



@app.route('/kriteria')
def kriteria():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM kriteria")
    data_kriteria = cur.fetchall()
    cur.close()

    return render_template('kriteria.html', kriteria=data_kriteria)

@app.route('/penilaian')
def penilaian():
    data_penilaian = [
        {'kriteria': 'Jarak', 'keterangan': 'Dekat', 'nilai': 3},
        {'kriteria': 'Jarak', 'keterangan': 'Sedang', 'nilai': 2},
        {'kriteria': 'Jarak', 'keterangan': 'Jauh', 'nilai': 1},

        {'kriteria': 'Fasilitas', 'keterangan': 'Lengkap', 'nilai': 3},
        {'kriteria': 'Fasilitas', 'keterangan': 'Cukup', 'nilai': 2},
        {'kriteria': 'Fasilitas', 'keterangan': 'Kurang', 'nilai': 1},

        {'kriteria': 'Reputasi', 'keterangan': 'Sangat Baik', 'nilai': 3},
        {'kriteria': 'Reputasi', 'keterangan': 'Baik', 'nilai': 2},
        {'kriteria': 'Reputasi', 'keterangan': 'Cukup', 'nilai': 1},
    ]

    return render_template('penilaian.html', penilaian=data_penilaian)

if __name__ == '__main__':
    app.run(debug=True)