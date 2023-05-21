import json
import re
from datetime import datetime


with open('DataEngineeringQ2.json') as file:
    json_data = json.load(file)


def calculate_age(dob):
    if dob is None:
        return None

    dob = datetime.fromisoformat(dob[:-5])
    today = datetime.now()
    age = today.year - dob.year


    if today.month < dob.month or (today.month == dob.month and today.day < dob.day):
        age -= 1

    return age

selected_data = []
for appointment in json_data:
    dob = appointment['patientDetails'].get('birthDate')
    age = calculate_age(dob)

    selected_data.append({
        'appointmentId': appointment['appointmentId'],
        'phoneNumber': appointment['phoneNumber'],
        'firstName': appointment['patientDetails']['firstName'],
        'lastName': appointment['patientDetails']['lastName'],
        'fullName': appointment['patientDetails']['firstName'] + ' ' + appointment['patientDetails']['lastName'],
        'gender': appointment['patientDetails'].get('gender'),
        'DOB': dob,
        'Age': age,
        'medicines': appointment['consultationData']['medicines']
    })


for item in selected_data:
    print(item)
