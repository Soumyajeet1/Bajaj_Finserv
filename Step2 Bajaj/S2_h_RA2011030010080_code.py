import json

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

for appointment in json_data:
    appointment_data = {
    'Age': calculate_age(appointment.get('birthDate')),
    'gender': appointment['patientDetails'].get('gender'),
    'validPhoneNumbers': valid_phone_numbers,
    'appointments': num_appointments,
    'medicines': num_medicines,
    'activeMedicines': num_active_medicines
}

# Specify the output file path
output_file = 'aggregated_data.json'

# Export the data to a JSON file
with open(output_file, 'w') as file:
    json.dump(data, file, indent=4)

print(f"Aggregated data exported to {output_file} successfully.")
