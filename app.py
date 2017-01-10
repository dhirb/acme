"""
Sample REST APIs for patient data
"""

#!flask/bin/python
from flask import Flask, jsonify, abort, make_response, request
import bleach, json
from helper import load, find_patient

app = Flask(__name__)

patients = []

"""
Error 404 handler

Returns
-------
json
    Error message that indicates the patient to search for does not exist
"""
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Patient not found'}), 404)

"""
Error 400 handler

Returns
-------
json
    Error message that indicates the patient creation has failed
"""
@app.errorhandler(400)
def cannot_create(error):
    return make_response(jsonify({'error': 'Cannot create new patient'}), 400)


"""
GET method that retrieves a patient's data given the patient ID

Parameters
----------
patient_id: int
    The given patient ID

Returns
-------
json
    The patient data if the patient to look for exists, error 404 otherwise
"""
@app.route('/acme/patient/<int:patient_id>', methods = ['GET'])
def get_patient(patient_id):
    # Get the latest patient data from file
    patients = load()
        
    # Search for patient
    patient = find_patient(patients, patient_id)

    if not patient:  # Patient not found
        abort(404)
        
    return jsonify({'patient': patient})


"""
POST method that creates a new patient with the data provided

Returns
-------
json
    The newly created patient ID, error 400 if patient creation has failed
"""
@app.route('/acme/patient', methods = ['POST'])
def create_patient():
    # Validate parameters
    if not request.json or not 'fullname' or not 'age' in request.json:
        abort(400)

    # Get the latest patient data from file before creating
    patients = load()
        
    # Sanitize input
    try:
        # Validate name
        fullname = bleach.clean(request.json['fullname'],
                                strip = False,
                                strip_comments = True)
        fullname = fullname.strip()

        # Check for empty name
        if len(fullname) <= 0:
            abort(400)


        # Validate age
        age = bleach.clean(request.json['age'],
                                strip = False,
                                strip_comments = True)

        # Check for valid age range
        if not 0 < int(age) < 130:
            abort(400)
            
    except:
        abort(400)

    # Special ID handling for the first patient
    if not patients:
        patient_id = 1
    else:
        patient_id = patients[-1]['id'] + 1
        
    # Add new patient to array
    new_patient = {
        'id': patient_id,
        'fullname': fullname,
        'age': age
    }
    patients.append(new_patient)

    # Write updated array to file
    try:
        with open('data.json', 'w') as f:
            json.dump(patients, f)
    except:
        abort(400)

    # Return new ID
    return jsonify({'id': patient_id}), 201



if __name__ == '__main__':
    app.run(debug=True)



