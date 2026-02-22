from .database import db

class Patient(db.Model):
    __tablename__ = 'patients'

    patient_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    password_hash = db.Column(db.String, nullable=False)
    phone = db.Column(db.String)
    age = db.Column(db.Integer)
    gender = db.Column(db.String)

class Doctor(db.Model):
    __tablename__ = 'doctors'

    doctor_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    password_hash = db.Column(db.String, nullable=False)
    specialization = db.Column(db.String, nullable=False)
    experience = db.Column(db.Integer)
    available_days = db.Column(db.String)
    available_time_slots = db.Column(db.String)

class Appointment(db.Model):
    __tablename__ = 'appointments'

    appointment_id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey("patients.patient_id"))
    doctor_id = db.Column(db.Integer, db.ForeignKey("doctors.doctor_id"))
    date = db.Column(db.String)
    time = db.Column(db.String)
    status = db.Column(db.String)
    reason_for_visit = db.Column(db.String)

    patient = db.relationship("Patient")
    doctor = db.relationship("Doctor")
