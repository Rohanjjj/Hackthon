from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)
    profession = db.Column(db.String(100), nullable=False)

class Doctor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)
    specialization = db.Column(db.String(100), nullable=False)
    license_number = db.Column(db.String(100), nullable=False)
    hospital_affiliation = db.Column(db.String(100), nullable=False)

class Server(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    ip_address = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100), nullable=False)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'user_form' in request.form:
            user = User(
                name=request.form['name'],
                email=request.form['email'],
                password=request.form['password'],
                profession=request.form['profession']
            )
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('index'))

        if 'doctor_form' in request.form:
            doctor = Doctor(
                name=request.form['name'],
                email=request.form['email'],
                password=request.form['password'],
                specialization=request.form['specialization'],
                license_number=request.form['license_number'],
                hospital_affiliation=request.form['hospital_affiliation']
            )
            db.session.add(doctor)
            db.session.commit()
            return redirect(url_for('index'))

        if 'server_form' in request.form:
            server = Server(
                name=request.form['name'],
                ip_address=request.form['ip_address'],
                location=request.form['location']
            )
            db.session.add(server)
            db.session.commit()
            return redirect(url_for('index'))

    return render_template('index.html')

@app.route('/print_data')
def print_data():
    users = User.query.all()
    doctors = Doctor.query.all()
    servers = Server.query.all()

    for user in users:
        print(f'User: {user.name}, Email: {user.email}, Profession: {user.profession}')

    for doctor in doctors:
        print(f'Doctor: {doctor.name}, Email: {doctor.email}, Specialization: {doctor.specialization}, License Number: {doctor.license_number}, Hospital Affiliation: {doctor.hospital_affiliation}')

    for server in servers:
        print(f'Server: {server.name}, IP Address: {server.ip_address}, Location: {server.location}')

    return 'Data printed to console'

if __name__ == '__main__':
    app.run(debug=True)
