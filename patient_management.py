class Patient:
    def __init__(self, name, age, disease):
        self.name = name
        self.age = age
        self.disease = disease


def search_patients_by_disease(patients, disease):
    return [patient.name for patient in patients if patient.disease == disease]


patients_data = [
    {"Name": "Alice", "Age": 30, "Disease": "Flu"},
    {"Name": "Bob", "Age": 45, "Disease": "Diabetes"},
    {"Name": "Charlie", "Age": 35, "Disease": "Flu"}
]

patients = [
    Patient(p["Name"], p["Age"], p["Disease"])
    for p in patients_data
]

search_disease = "Flu"

result = search_patients_by_disease(patients, search_disease)

print(f"Patients with {search_disease}:", result)
