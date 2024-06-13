from flask import Flask, request

app = Flask(__name__)

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

@app.route('/')
def home():
    return '''
    <h1>Search API</h1>
    <form id="searchForm">
        <label for="target">Enter a Number to Search:</label>
        <input type="text" id="target" name="target" required>
        <button type="submit">Search</button>
    </form>
    <p id="result"></p>
    <script>
        document.getElementById('searchForm').addEventListener('submit', function(event) {
            event.preventDefault();  // Prevent the form from submitting via the browser
            var target = document.getElementById('target').value;
            fetch(`/search?target=${target}`)
                .then(response => response.text())  // Assuming response is plain text
                .then(text => document.getElementById('result').textContent = text)
                .catch(err => document.getElementById('result').textContent = 'Error: ' + err);
        });
    </script>
    '''

@app.route('/search', methods=['GET'])
def search():
    nums = [2, 5, 5, 5, 6, 6, 8, 9, 9, 9]  # Predefined list of numbers
    target = request.args.get('target', type=int)
    
    if target is None:
        return "Search Box Cannot Be Empty. Please Enter a Number..!!!", 400

    if target not in nums:
        return "The number is not in the list. Please try another number.", 404
    
    index = find_first_occurrence(nums, target)
    if index == -1:
        return "The number is not in the list.", 404
    return f"The First Occurrence of {target} is at Index {index} Which is Position {index + 1}"

if __name__ == '__main__':
    app.run(debug=True)
