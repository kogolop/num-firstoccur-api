from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Conversion factors
LENGTH_CONVERSIONS = {
    "m_to_ft": 3.28084,
    "ft_to_m": 0.3048,
    "km_to_miles": 0.621371,
    "miles_to_km": 1.60934
}

WEIGHT_CONVERSIONS = {
    "kg_to_lbs": 2.20462,
    "lbs_to_kg": 0.453592,
    "g_to_oz": 0.035274,
    "oz_to_g": 28.3495
}

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

@app.route('/api/convert', methods=['POST'])
def convert():
    data = request.json
    if not data or 'value' not in data or 'from_unit' not in data or 'to_unit' not in data:
        return jsonify({"error": "Invalid input. Please provide 'value', 'from_unit', and 'to_unit'."}), 400

    try:
        value = float(data['value'])
    except ValueError:
        return jsonify({"error": "Invalid value. Please provide a numeric value."}), 400

    from_unit = data['from_unit']
    to_unit = data['to_unit']

    # Length conversions
    if f"{from_unit}_to_{to_unit}" in LENGTH_CONVERSIONS:
        result = value * LENGTH_CONVERSIONS[f"{from_unit}_to_{to_unit}"]
        return jsonify({
            "from_value": value,
            "from_unit": from_unit,
            "to_value": result,
            "to_unit": to_unit
        })

    # Weight conversions
    if f"{from_unit}_to_{to_unit}" in WEIGHT_CONVERSIONS:
        result = value * WEIGHT_CONVERSIONS[f"{from_unit}_to_{to_unit}"]
        return jsonify({
            "from_value": value,
            "from_unit": from_unit,
            "to_value": result,
            "to_unit": to_unit
        })

    # Temperature conversions
    if from_unit == "celsius" and to_unit == "fahrenheit":
        result = celsius_to_fahrenheit(value)
        return jsonify({
            "from_value": value,
            "from_unit": from_unit,
            "to_value": result,
            "to_unit": to_unit
        })
    elif from_unit == "fahrenheit" and to_unit == "celsius":
        result = fahrenheit_to_celsius(value)
        return jsonify({
            "from_value": value,
            "from_unit": from_unit,
            "to_value": result,
            "to_unit": to_unit
        })

    return jsonify({"error": "Unsupported conversion."}), 400

@app.route('/api/units', methods=['GET'])
def get_units():
    units = {
        "length": ["m", "ft", "km", "miles"],
        "weight": ["kg", "lbs", "g", "oz"],
        "temperature": ["celsius", "fahrenheit"]
    }
    return jsonify(units)

@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Not found. Please check the API endpoint."}), 404

@app.errorhandler(405)
def method_not_allowed(error):
    return jsonify({"error": "Method not allowed. Please use POST for conversions and GET for unit list."}), 405

if __name__ == '__main__':
    app.run(debug=True, port=5004)  # Using port 5004 to avoid conflicts