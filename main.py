from patient import Patient
from disease_detector import detect_disease
from database import save_patient
from report import generate_report


def main():

    print("===== Silent Disease Detection System =====")

    name = input("Enter Patient Name: ")
    age = int(input("Enter Age: "))
    bp = int(input("Enter Blood Pressure: "))
    sugar = int(input("Enter Sugar Level: "))
    cholesterol = int(input("Enter Cholesterol Level: "))

    patient = Patient(name, age, bp, sugar, cholesterol)

    result = detect_disease(bp, sugar, cholesterol)

    save_patient(patient.get_data())

    generate_report(patient, result)


if __name__ == "__main__":
    main()