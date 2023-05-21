import json
import re
import hashlib


with open('DataEngineeringQ2.json') as file:
    json_data = json.load(file)

def is_valid_mobile(phone_number):

    pattern = r'^(?:\+91|91)?[6-9]\d{9}$'
    return bool(re.match(pattern, phone_number))


def calculate_hash(data):
    return hashlib.sha256(data.encode()).hexdigest()


selected_data = []
for appointment in json_data:
    phone_number = appointment['phoneNumber']
    is_valid = is_valid_mobile(phone_number)
    phone_number_hash = calculate_hash(phone_number) if is_valid else None

    selected_data.append({
        'appointmentId': appointment['appointmentId'],
        'phoneNumber': phone_number,
        'firstName': appointment['patientDetails']['firstName'],
        'lastName': appointment['patientDetails']['lastName'],
        'fullName': appointment['patientDetails']['firstName'] + ' ' + appointment['patientDetails']['lastName'],
        'isValidMobile': is_valid,
        'phoneNumberHash': phone_number_hash,
        'gender': appointment['patientDetails'].get('gender'),
        'DOB': appointment['patientDetails'].get('birthDate'),
        'medicines': appointment['consultationData']['medicines']
    })

for item in selected_data:
    print(item)
