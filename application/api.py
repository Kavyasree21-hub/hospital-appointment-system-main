from flask_restful import Resource, reqparse
from application.models import Patient, Doctor, Appointment
from application.database import db
from werkzeug.security import generate_password_hash, check_password_hash
register_parser = reqparse.RequestParser()
register_parser.add_argument("role", required=True)
register_parser.add_argument("name", required=True)
register_parser.add_argument("email", required=True)
register_parser.add_argument("password", required=True)

# patient only
register_parser.add_argument("phone")
register_parser.add_argument("age")
register_parser.add_argument("gender")

# doctor only
register_parser.add_argument("specialization")
register_parser.add_argument("experience")
register_parser.add_argument("available_days")
register_parser.add_argument("available_time_slots")


class RegisterAPI(Resource):
    def post(self):
        data = register_parser.parse_args()
        role = data["role"].lower()

        # ------------ PATIENT REGISTRATION ------------
        if role == "patient":
            if Patient.query.filter_by(email=data["email"]).first():
                return {"message": "Email already exists"}, 400

            new_user = Patient(
                name=data["name"],
                email=data["email"],
                phone=data.get("phone"),
                age=data.get("age"),
                gender=data.get("gender"),
                password_hash=generate_password_hash(data["password"])
            )

        # ------------ DOCTOR REGISTRATION ------------
        elif role == "doctor":
            if Doctor.query.filter_by(email=data["email"]).first():
                return {"message": "Email already exists"}, 400

            new_user = Doctor(
                name=data["name"],
                email=data["email"],
                password_hash=generate_password_hash(data["password"]),
                specialization=data.get("specialization"),
                experience=data.get("experience"),
                available_days=data.get("available_days"),
                available_time_slots=data.get("available_time_slots")
            )

        else:
            return {"message": "Invalid role"}, 400

        db.session.add(new_user)
        db.session.commit()
        return {"message": "Registration successful!"}, 201
login_parser = reqparse.RequestParser()
login_parser.add_argument("email", required=True)
login_parser.add_argument("password", required=True)


class LoginAPI(Resource):
    def post(self):
        data = login_parser.parse_args()

        # check patient first
        user = Patient.query.filter_by(email=data["email"]).first()
        role = "patient"

        # else check doctor
        if user is None:
            user = Doctor.query.filter_by(email=data["email"]).first()
            role = "doctor"

        if not user:
            return {"message": "User not found"}, 404

        if not check_password_hash(user.password_hash, data["password"]):
            return {"message": "Incorrect password"}, 401

        user_id = user.patient_id if role == "patient" else user.doctor_id

        return {
            "message": "Login successful",
            "id": user_id,
            "role": role
        }, 200
book_parser = reqparse.RequestParser()
book_parser.add_argument("doctor_id", required=True, type=int)
book_parser.add_argument("patient_id", required=True, type=int)
book_parser.add_argument("date", required=True)
book_parser.add_argument("time", required=True)
book_parser.add_argument("reason_for_visit", required=False)

class BookAppointmentAPI(Resource):
    def post(self):
        data = book_parser.parse_args()

        appointment = Appointment(
            doctor_id=data["doctor_id"],
            patient_id=data["patient_id"],
            date=data["date"],
            time=data["time"],
            status="booked",
            reason_for_visit=data.get("reason_for_visit")
        )

        db.session.add(appointment)
        db.session.commit()
        return {"message": "Appointment booked successfully"}, 201
class PatientAppointmentsAPI(Resource):
    def get(self, patient_id):
        appts = Appointment.query.filter_by(patient_id=patient_id).all()

        return [{
            "appointment_id": a.appointment_id,
            "doctor_id": a.doctor_id,
            "date": a.date,
            "time": a.time,
            "status": a.status,
            "reason_for_visit": a.reason_for_visit
        } for a in appts], 200
class DoctorAppointmentsAPI(Resource):
    def get(self, doctor_id):
        appts = Appointment.query.filter_by(doctor_id=doctor_id).all()

        return [{
            "appointment_id": a.appointment_id,
            "patient_id": a.patient_id,
            "date": a.date,
            "time": a.time,
            "status": a.status,
            "reason_for_visit": a.reason_for_visit
        } for a in appts], 200
