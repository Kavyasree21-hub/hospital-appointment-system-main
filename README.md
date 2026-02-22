# Hospital Appointment System

A full-stack web application for managing hospital appointments between patients and doctors. This project demonstrates expertise in **backend development**, **database design**, **API development**, and **web application architecture**.

---

## 🎯 Project Overview

This is a **Flask-based web application** that allows:
- **Patients** to register, login, book appointments, and view their appointment history
- **Doctors** to register, login, view patient appointments, and manage schedules
- **Admin functionality** for managing the appointment system

---

## 🔧 Tech Stack & Skills Demonstrated

### Backend & Framework
- **Python 3** - Core language
- **Flask** - Web framework for routing and request handling
- **Flask-RESTful** - REST API development
- **Flask-SQLAlchemy** - ORM for database operations

### Database
- **SQLite3** - Relational database
- **SQL Queries** - Complex joins and filtering
- **Database Relationships** - Foreign keys and relationships

### Frontend
- **HTML5** - Semantic markup
- **CSS3** - Styling and responsive design
- **Jinja2 Templates** - Template rendering

### Security
- **Password Hashing** - Using Werkzeug security
- **Session Management** - User authentication and authorization
- **Input Validation** - Form validation and error handling

### Tools & Practices
- **Git Version Control** - Commit history and branching
- **RESTful API Design** - Clean endpoint structure
- **MVC Architecture** - Separation of concerns
- **Error Handling** - Comprehensive error management

---

## 📁 Project Structure

```
hospital-appointment-system/
├── application/
│   ├── __init__.py          # App initialization
│   ├── api.py              # REST API endpoints
│   ├── controller.py       # Route handlers and business logic
│   ├── models.py           # Database models (Patient, Doctor, Appointment)
│   ├── database.py         # Database configuration
│   ├── config.py           # Application configuration
│   └── validation.py       # Input validation
├── templates/
│   ├── base.html           # Base template
│   ├── login.html          # Login page
│   ├── register.html       # Registration page
│   ├── dashboard.html      # Main dashboard
│   ├── dashboard_patient.html    # Patient dashboard
│   ├── dashboard_doctor.html     # Doctor dashboard
│   ├── book_appointment.html     # Appointment booking
│   ├── my_appointments.html      # Patient's appointments
│   └── doctor_appointments.html  # Doctor's appointments
├── main.py                 # Application entry point
├── requirements.txt        # Python dependencies
├── .gitignore             # Git ignore rules
└── README.md              # Project documentation
```

---

## 🚀 Features

### Patient Features
✅ User registration with email validation  
✅ Secure login with password hashing  
✅ Book appointments with available doctors  
✅ View all booked appointments  
✅ Appointment status tracking  

### Doctor Features
✅ Doctor profile registration  
✅ View all patient appointments  
✅ Manage appointment schedule  
✅ Accept/reject appointments  

### System Features
✅ Role-based access control (Patient/Doctor)  
✅ Session management  
✅ Database persistence  
✅ Error handling and validation  
✅ RESTful API endpoints  

---

## 💾 Database Schema

### Patients Table
```sql
CREATE TABLE patients (
    patient_id INTEGER PRIMARY KEY,
    name VARCHAR NOT NULL,
    email VARCHAR UNIQUE NOT NULL,
    password_hash VARCHAR NOT NULL,
    phone VARCHAR,
    age INTEGER,
    gender VARCHAR
);
```

### Doctors Table
```sql
CREATE TABLE doctors (
    doctor_id INTEGER PRIMARY KEY,
    name VARCHAR NOT NULL,
    email VARCHAR UNIQUE NOT NULL,
    password_hash VARCHAR NOT NULL,
    specialization VARCHAR NOT NULL,
    experience INTEGER,
    available_days VARCHAR,
    available_time_slots VARCHAR
);
```

### Appointments Table
```sql
CREATE TABLE appointments (
    appointment_id INTEGER PRIMARY KEY,
    patient_id INTEGER FOREIGN KEY,
    doctor_id INTEGER FOREIGN KEY,
    date VARCHAR,
    time VARCHAR,
    status VARCHAR,
    reason_for_visit VARCHAR
);
```

---

## 📋 Installation & Setup

### Prerequisites
- Python 3.8+
- pip (Python package manager)

### Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/Kavyasree21-hub/hospital-appointment-system.git
   cd hospital-appointment-system
   ```

2. **Create virtual environment** (Optional but recommended)
   ```bash
   python -m venv venv
   source venv/Scripts/activate  # On Windows
   source venv/bin/activate       # On Mac/Linux
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python main.py
   ```

5. **Access the application**
   - Open your browser and go to: `http://localhost:8080`

---

## 🔌 API Endpoints

### Authentication
- `POST /api/register` - Register new user (Patient/Doctor)
- `POST /api/login` - User login

### Patient Endpoints
- `GET /book` - View available doctors
- `POST /book` - Book appointment
- `GET /my_appointments` - View patient's appointments
- `GET /dashboard/patient` - Patient dashboard

### Doctor Endpoints
- `GET /doctor_appointments` - View doctor's appointments
- `GET /dashboard/doctor` - Doctor dashboard

### General
- `GET /` - Home/Login page
- `GET /logout` - Logout user

---

## 🔒 Security Features Implemented

✅ **Password Hashing** - Passwords hashed using Werkzeug security  
✅ **Session Management** - Flask sessions for user authentication  
✅ **Input Validation** - Form validation on registration and booking  
✅ **Role-Based Access Control** - Different access levels for Patient/Doctor  
✅ **CSRF Protection** - Form security measures  

---

## 🎓 Key Skills Demonstrated

| Skill | Implementation |
|-------|-----------------|
| **Backend Development** | Flask routing, request handling, business logic |
| **Database Design** | Normalized schema, relationships, foreign keys |
| **ORM Usage** | SQLAlchemy models and queries |
| **REST API Design** | Clean endpoints, proper HTTP methods |
| **Authentication** | Password hashing, session management |
| **Frontend Integration** | Jinja2 templates, HTML forms |
| **Git & Version Control** | Repository management, commits |
| **Code Organization** | MVC pattern, separation of concerns |
| **Error Handling** | Try-catch blocks, validation |
| **Documentation** | Code comments, README, inline documentation |

---

## 🔄 Workflow Example

**Patient Journey:**
1. Register → 2. Login → 3. View Doctors → 4. Book Appointment → 5. Check Status → 6. Logout

**Doctor Journey:**
1. Register → 2. Login → 3. View Appointments → 4. Manage Status → 5. Logout

---

## 📊 Code Quality Highlights

- ✅ Clear separation of concerns (MVC architecture)
- ✅ Reusable components and functions
- ✅ Proper error handling and logging
- ✅ Input validation and sanitization
- ✅ Secure password management
- ✅ Clean and readable code structure

---

## 🚀 Future Enhancements

- Email notifications for appointment confirmations
- SMS reminders for scheduled appointments
- Advanced scheduling with time slots
- Payment integration
- User profile editing
- Appointment cancellation and rescheduling
- Admin dashboard
- Email verification
- Multi-language support

---

## 📝 License

This project is open source and available under the MIT License.

---

## 👤 Author

**Kavyasree**  
GitHub: [Kavyasree21-hub](https://github.com/Kavyasree21-hub)  
Project: [Hospital Appointment System](https://github.com/Kavyasree21-hub/hospital-appointment-system)

---

## 💬 Contact & Support

For questions or suggestions, feel free to open an issue on GitHub or contact me directly.

---

**Last Updated:** February 2026
