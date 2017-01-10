"""
Helper functions
"""

import json
from pathlib import Path

"""
Loads patient data from data.json

Returns
-------
json
    Patient data in json if patient exists, empty array otherwise
"""
def load():
    data_file = Path('data.json')

    # Create new file if not exist
    if not data_file.is_file():
        f = open('data.json', 'x')
        return []

    # Else, load patient data
    try:
        with open('data.json', 'r') as f:
            return json.load(f)
    except:
        return []


"""
Search patient by ID

Parameters
----------
patients: array
    The array of all patient data
patient_id: int
    The patient ID

Returns
-------
json
    Patient data in json if patient exists, empty array otherwise
"""
def find_patient(patients, patient_id):
    patient = [patient for patient in patients if patient['id'] == patient_id]

    if len(patient) == 0:  # Patient not found
        return []

    return patient[0]
