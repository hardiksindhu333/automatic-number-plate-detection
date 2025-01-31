from flask import Flask, jsonify, render_template
import csv
import os

app = Flask(__name__)

# Load data from CSV
def load_parking_data():
    parking_data = []
    file_path = '/home/hardik/project/automatic-number-plate-recognition-python-yolov8/interpolate(1).csv'  # Ensure this path is correct and includes the .csv extension
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file '{file_path}' does not exist. Please check the file path.")

    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            parking_data.append({
                "license_number": row["license_number"]
            })
    return parking_data

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_parking_slots', methods=['GET'])
def get_parking_slots():
    try:
        data = load_parking_data()
        slots = []
        slot_number = 1
        license_to_slot = {}

        for entry in data:
            license_number = entry["license_number"]
            if license_number not in license_to_slot:
                license_to_slot[license_number] = slot_number
                slot_number += 1

            slots.append({
                "slot_number": license_to_slot[license_number],
                "license_number": license_number
            })

        return jsonify({"slots": slots})
    except FileNotFoundError as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
