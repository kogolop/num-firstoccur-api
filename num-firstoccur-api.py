from flask import Flask, request, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)

def generate_random_numbers():
    # Generate a list of 20 random numbers between 1 and 100
    nums = [random.randint(1, 100) for _ in range(20)]
    # Sort the list to allow binary search
    return sorted(nums)

def find_first_occurrence(nums, target):
    left, right = 0, len(nums) - 1
    result = -1
    while left <= right:
        mid = (left + right) // 2
        if target > nums[mid]:
            left = mid + 1
        elif target < nums[mid]:
            right = mid - 1
        else:
            result = mid
            right = mid - 1  # Continue searching to the left.
    return result

@app.route('/api/search', methods=['POST'])
def search():
    data = request.json
    if not data or 'target' not in data:
        return jsonify({"error": "Invalid input. Please provide a 'target' number."}), 400

    try:
        target = int(data['target'])
    except ValueError:
        return jsonify({"error": "Invalid input. 'target' must be a valid integer."}), 400

    nums = generate_random_numbers()
    index = find_first_occurrence(nums, target)
    
    if index == -1:
        return jsonify({
            "error": "The number is not in the list.",
            "numbers": nums
        }), 404
    
    return jsonify({
        "target": target,
        "index": index,
        "position": index + 1,
        "message": f"The First Occurrence of {target} is at Index {index} Which is Position {index + 1}",
        "numbers": nums
    }), 200

@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Not found. Please check the API endpoint."}), 404

@app.errorhandler(405)
def method_not_allowed(error):
    return jsonify({"error": "Method not allowed. Please use POST for this endpoint."}), 405

if __name__ == '__main__':
    app.run(debug=True, port=5003)