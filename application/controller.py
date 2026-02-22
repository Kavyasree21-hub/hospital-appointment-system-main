from flask import render_template, request, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
from application.models import Patient, Doctor, Appointment
from application.database import db
from flask import current_app as app

# -------------------------------
# HOME PAGE
# -------------------------------
@app.route("/")
def home():
    return render_template("login.html")

# -------------------------------
# REGISTER
# -------------------------------
@app.route("/register", methods=["GET","POST"])
def register():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        password = generate_password_hash(request.form["password"])
        role = request.form["role"]

        if role == "patient":
            user = Patient(name=name, email=email, password_hash=password)
        else:
            user = Doctor(name=name, email=email, specialization="General", password_hash=password)

        db.session.add(user)
        db.session.commit()

        flash("Registration successful!", "success")
        return redirect(url_for("login"))

    return render_template("register.html")

# -------------------------------
# LOGIN
# -------------------------------
@app.route("/login", methods=["GET","POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        # First try patient
        user = Patient.query.filter_by(email=email).first()
        role = "patient"

        # If not patient, try doctor
        if not user:
            user = Doctor.query.filter_by(email=email).first()
            role = "doctor"

        if not user or not check_password_hash(user.password_hash, password):
            flash("Invalid email or password", "danger")
            return redirect(url_for("login"))

        session["user_id"] = user.patient_id if role == "patient" else user.doctor_id
        session["role"] = role

        return redirect(url_for("dashboard"))

    return render_template("login.html")

# -------------------------------
# MAIN DASHBOARD REDIRECTOR
# -------------------------------
@app.route("/dashboard")
def dashboard():
    if "role" not in session:
        return redirect(url_for("login"))

    if session["role"] == "patient":
        return redirect(url_for("dashboard_patient"))
    
    if session["role"] == "doctor":
        return redirect(url_for("dashboard_doctor"))

# -------------------------------
# PATIENT DASHBOARD
# -------------------------------
@app.route("/dashboard/patient")
def dashboard_patient():
    if session.get("role") != "patient":
        return redirect(url_for("login"))

    patient_id = session["user_id"]

    # fetch patient's appointments with doctor name
    appointments = (
        db.session.query(Appointment, Doctor.name.label("doctor_name"))
        .join(Doctor, Appointment.doctor_id == Doctor.doctor_id)
        .filter(Appointment.patient_id == patient_id)
        .all()
    )

    return render_template("dashboard_patient.html", appointments=appointments)

# -------------------------------
# DOCTOR DASHBOARD
# -------------------------------
@app.route("/dashboard/doctor")
def dashboard_doctor():
    if session.get("role") != "doctor":
        return redirect(url_for("login"))

    doctor_id = session["user_id"]

    appointments = (
        db.session.query(
            Appointment.date,
            Appointment.time,
            Appointment.status,
            Patient.name.label("patient_name")
        )
        .join(Patient, Appointment.patient_id == Patient.patient_id)
        .filter(Appointment.doctor_id == doctor_id)
        .all()
    )

    return render_template("dashboard_doctor.html", appointments=appointments)

# -------------------------------
# BOOK APPOINTMENT (PATIENT ONLY)
# -------------------------------
@app.route("/book", methods=["GET","POST"])
def book_appointment():
    if session.get("role") != "patient":
        return redirect(url_for("login"))

    doctors = Doctor.query.all()

    if request.method == "POST":
        appointment = Appointment(
            patient_id=session["user_id"],
            doctor_id=request.form["doctor_id"],
            date=request.form["date"],
            time=request.form["time"],
            status="booked"
        )

        db.session.add(appointment)
        db.session.commit()

        flash("Appointment booked successfully!", "success")
        return redirect(url_for("my_appointments"))

    return render_template("book_appointment.html", doctors=doctors)

# -------------------------------
# PATIENT → VIEW APPOINTMENTS
# -------------------------------
@app.route("/my_appointments")
def my_appointments():
    appointments = Appointment.query.filter_by(patient_id=session["user_id"]).all()
    return render_template("my_appointments.html", appointments=appointments)

# -------------------------------
# DOCTOR → VIEW APPOINTMENTS
# -------------------------------
@app.route("/doctor_appointments")
def doctor_appointments():
    appointments = Appointment.query.filter_by(doctor_id=session["user_id"]).all()
    return render_template("doctor_appointments.html", appointments=appointments)

# -------------------------------
# LOGOUT
# -------------------------------
@app.route("/logout")
def logout():
    session.clear()
    flash("Logged out!", "info")
    return redirect(url_for("login"))
