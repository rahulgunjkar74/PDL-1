import csv

FILE = "data/patient_data.csv"

def save_patient(data):

    with open(FILE,"a",newline="") as file:

        writer = csv.writer(file)

        writer.writerow(data)


def get_all_patients():

    with open(FILE,"r") as file:

        reader = csv.reader(file)

        data = list(reader)

    return data


def delete_patient(index):

    rows = []

    with open(FILE,"r") as file:

        reader = csv.reader(file)

        rows = list(reader)

    rows.pop(index)

    with open(FILE,"w",newline="") as file:

        writer = csv.writer(file)

        writer.writerows(rows)