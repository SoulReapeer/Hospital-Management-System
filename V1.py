# Data storage
patients = []
doctors = []
appointments = []

# Models
class Patient:
    def __init__(self, patient_id, name, age, gender, illness):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.gender = gender
        self.illness = illness

class Doctor:
    def __init__(self, doctor_id, name, specialty):
        self.doctor_id = doctor_id
        self.name = name
        self.specialty = specialty

class Appointment:
    def __init__(self, appointment_id, patient_name, doctor_name, date):
        self.appointment_id = appointment_id
        self.patient_name = patient_name
        self.doctor_name = doctor_name
        self.date = date

# Utility function
def find_by_id(records, attr, value):
    return next((record for record in records if getattr(record, attr) == value), None)

# Patient Management
def add_patient():
    pid = input("Patient ID: ")
    name = input("Name: ")
    age = input("Age: ")
    gender = input("Gender: ")
    illness = input("Illness: ")
    patients.append(Patient(pid, name, age, gender, illness))
    print("Patient added.\n")

def list_patients():
    if not patients:
        print("No patients found.\n")
        return
    for p in patients:
        print(f"ID: {p.patient_id}, Name: {p.name}, Age: {p.age}, Gender: {p.gender}, Illness: {p.illness}")
    print()

def delete_patient():
    pid = input("Enter Patient ID to delete: ")
    patient = find_by_id(patients, "patient_id", pid)
    if patient:
        patients.remove(patient)
        print("Patient deleted.\n")
    else:
        print("Patient not found.\n")

# Doctor Management
def add_doctor():
    did = input("Doctor ID: ")
    name = input("Name: ")
    specialty = input("Specialty: ")
    doctors.append(Doctor(did, name, specialty))
    print("Doctor added.\n")

def list_doctors():
    if not doctors:
        print("No doctors found.\n")
        return
    for d in doctors:
        print(f"ID: {d.doctor_id}, Name: {d.name}, Specialty: {d.specialty}")
    print()

def delete_doctor():
    did = input("Enter Doctor ID to delete: ")
    doctor = find_by_id(doctors, "doctor_id", did)
    if doctor:
        doctors.remove(doctor)
        print("Doctor deleted.\n")
    else:
        print("Doctor not found.\n")

# Appointment Management
def schedule_appointment():
    aid = input("Appointment ID: ")
    patient_name = input("Patient Name: ")
    doctor_name = input("Doctor Name: ")
    date = input("Appointment Date (YYYY-MM-DD): ")
    appointments.append(Appointment(aid, patient_name, doctor_name, date))
    print("Appointment scheduled.\n")

def list_appointments():
    if not appointments:
        print("No appointments found.\n")
        return
    for a in appointments:
        print(f"ID: {a.appointment_id}, Patient: {a.patient_name}, Doctor: {a.doctor_name}, Date: {a.date}")
    print()

# Main Menu
def menu():
    while True:
        print("=== Hospital Management System ===")
        print("1. Add Patient")
        print("2. List Patients")
        print("3. Delete Patient")
        print("4. Add Doctor")
        print("5. List Doctors")
        print("6. Delete Doctor")
        print("7. Schedule Appointment")
        print("8. List Appointments")
        print("0. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_patient()
        elif choice == "2":
            list_patients()
        elif choice == "3":
            delete_patient()
        elif choice == "4":
            add_doctor()
        elif choice == "5":
            list_doctors()
        elif choice == "6":
            delete_doctor()
        elif choice == "7":
            schedule_appointment()
        elif choice == "8":
            list_appointments()
        elif choice == "0":
            print("Exiting system.")
            break
        else:
            print("Invalid choice. Try again.\n")

# Run program
if __name__ == "__main__":
    menu()
