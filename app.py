from flask import Flask, render_template, request, redirect, send_file

from patient import Patient
from database import save_patient, get_all_patients, delete_patient
from ai_model import predict_disease, explain_prediction
from report_pdf import create_pdf

app = Flask(__name__)


# HOME PAGE
@app.route("/")
def home():
    return render_template("index.html")


# AI PREDICTION
@app.route("/predict", methods=["POST"])
def predict():

    name = request.form["name"]
    age = int(request.form["age"])
    bp = int(request.form["bp"])
    sugar = int(request.form["sugar"])
    cholesterol = int(request.form["cholesterol"])

    patient = Patient(name, age, bp, sugar, cholesterol)

    result = predict_disease(bp, sugar, cholesterol)

    explanation = explain_prediction(bp, sugar, cholesterol)

    save_patient(patient.get_data())

    return render_template(
        "index.html",
        result=result,
        name=name,
        explanation=explanation
    )


# DOCTOR LOGIN
@app.route("/login", methods=["GET","POST"])
def login():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        if username == "doctor" and password == "1234":
            return redirect("/dashboard")

    return render_template("login.html")


# DASHBOARD
@app.route("/dashboard")
def dashboard():

    patients = get_all_patients()
    patients = patients[1:]

    total = len(patients)

    bp_values = []
    sugar_values = []
    chol_values = []

    low = 0
    medium = 0
    high = 0

    for row in patients:

        try:

            bp = int(row[2])
            sugar = int(row[3])
            chol = int(row[4])

            bp_values.append(bp)
            sugar_values.append(sugar)
            chol_values.append(chol)

            if sugar < 120:
                low += 1
            elif sugar < 160:
                medium += 1
            else:
                high += 1

        except:
            continue

    avg_bp = sum(bp_values)/len(bp_values) if bp_values else 0
    avg_sugar = sum(sugar_values)/len(sugar_values) if sugar_values else 0
    avg_chol = sum(chol_values)/len(chol_values) if chol_values else 0

    return render_template(
        "dashboard.html",
        total=total,
        avg_bp=avg_bp,
        avg_sugar=avg_sugar,
        avg_chol=avg_chol,
        bp_values=bp_values,
        sugar_values=sugar_values,
        chol_values=chol_values,
        low=low,
        medium=medium,
        high=high,
        patients=patients
    )


# PDF REPORT
@app.route("/report/<name>/<age>/<bp>/<sugar>/<chol>")
def report(name, age, bp, sugar, chol):

    try:
        bp = int(bp)
        sugar = int(sugar)
        chol = int(chol)
    except:
        return redirect("/dashboard")

    result = predict_disease(bp, sugar, chol)

    filename = create_pdf(name, age, bp, sugar, chol, result)

    return send_file(filename, as_attachment=True)


# DELETE PATIENT
@app.route("/delete/<int:index>")
def delete(index):

    delete_patient(index + 1)

    return redirect("/dashboard")


if __name__ == "__main__":
    app.run(debug=True)