# Sample ACME REST API
## Created by Yuen Lye Yeap

## Usage
1. GET
  * Retrieves the patient information given the patient ID
  * Example usage
  `curl -X GET http://localhost:5000/acme/patient/1`
  * Example output
  ```
  {
  "patient": {
    "age": "25", 
    "fullname": "Yuen Lye Yeap", 
    "id": 1
  }
}
```
  
2. POST
  * Creates a new patient
  * Example usage
  `curl -i -H "Content-Type: application/json" -X POST -d "{"""fullname""":"""Yuen Lye Yeap""","""age""":25}" http://localhost:5000/acme/patient`
  * Example output
  ```
  {
      "id": 1
  }
  ```

## Considered but not done
1. Handling unique patient name
  * Since many patients share the same last name and first name, we should not discard duplicate names. Instead, we should differentiate the patients using unique patient IDs.
  
2. Scrambling patient ID
  * Scrambling patient ID is useful to mask the internal implementation (in this case, incrementing the ID every time a new patient is added). However, it is much more sound to implement this in the database (most database management system should have built-in functionality to do this). Since we are using a file-based storage and is not likely to be implemented in a real-world scenario, we maintain a simple approach to generating patient IDs.

## Framework used
1. Python (Windows)
2. Flask (REST)
3. Bleach (input validation)
