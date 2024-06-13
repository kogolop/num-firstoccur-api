# Num-FirstOccur-API

## Overview
Num-FirstOccur-API is a Flask-based web API designed to find the 
first occurrence of a number in a predefined list. This application 
is implemented in Python and provides a web interface using JavaScript
to interact with the API dynamically.
## Features
- Interactive web interface allowing users to input numbers.
- API endpoint that returns the first occurrence index and position,
 accessible via JavaScript.
- Efficient binary search algorithm implemented in Python.
- Error handling for non-existent numbers and empty input validation.
## Prerequisites
Before you can run this application, you'll need:
- Python 3.6 or higher
- Flask
## Installation
Clone the repository:
``git clone https://github.com/kogolop/num-firstoccur-api.git
 cd num-firstoccur-api
``
Install the necessary Python packages:
```
pip install Flask
```
## Running the Application
To run the application, use the following command from the root
directory of the project:
```
python app.py
```
This will start the Flask server on `http://127.0.0.1:5000/`.
## Usage
Navigate to `http://127.0.0.1:5000/` in your web browser to 
access the application. Enter a number to search for its first
occurrence in the predefined list. The application will display
the index of the first occurrence and its position in the list,
or an error message if the number is not found.

## API Endpoint
### Request
`GET /search?target=<number>`
### Parameters
- `target` (required): The number to search for in the list.
### Response
- Success: Returns the first occurrence of the number and its
  position in the list.
- Error: Returns an error message if the number is not in the
  list or if no number is provided.
## How It Works
The backend API is built using Flask, a lightweight Python web
framework. It provides a `/search` endpoint that performs a 
binary search to find the first occurrence of a number within 
a static list. The frontend utilizes JavaScript to handle user 
inputs, asynchronously calls the API, and displays the results 
without needing to reload the page.
## Contributing
Contributions to the Num-FirstOccur-API are welcome! Please
feel free to fork the repository, make your changes, and 
submit a pull request.
## License
This project is licensed under the MIT License - see the LICENSE file for details.

