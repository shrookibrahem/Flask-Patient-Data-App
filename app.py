from flask import Flask, request, render_template, redirect, url_for, flash
import sqlite3

app = Flask(__name__)
app.secret_key = 'your_secret_key'

def get_patient_by_user_id(user_id):
    conn = sqlite3.connect('patients.db')
    c = conn.cursor()
    c.execute("SELECT * FROM patients WHERE user_id = ?", (user_id,))
    patient = c.fetchone()
    conn.close()
    return patient

@app.route('/commoninfo')
def home():
    return render_template('index.html')

@app.route('/commoninfo/fetch', methods=['POST'])
def check_patient():
    user_id = request.form['user_id']
    patient = get_patient_by_user_id(user_id)

    if patient:
        return render_template('patient_details.html', patient=patient)
    else:
        return render_template('add_patient.html', user_id=user_id)

@app.route('/commoninfo/add', methods=['POST'])
def add_patient():
    user_name = request.form['user_name']
    password = request.form['password']
    date_of_birth = request.form['date_of_birth']
    firstname = request.form['firstname']
    lastname = request.form['lastname']

    conn = sqlite3.connect('patients.db')
    c = conn.cursor()
    c.execute('''
        INSERT INTO patients (user_name, password, date_of_birth, firstname, lastname)
        VALUES (?, ?, ?, ?, ?)
    ''', (user_name, password, date_of_birth, firstname, lastname))
    conn.commit()
    conn.close()
    flash("Patient has been successfully added!")
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True, port=8000)



