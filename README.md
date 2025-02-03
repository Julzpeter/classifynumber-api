# Number Classification API
This is a Django-based Api that classifies a given number and returns its mathematical properties along with a fun fact. The API is deployed and publicly accessible

## Features
Accepts a number as input and returns:

- Whether the number is prime
- Whether the number is perfect
- Whether the number is an Armstrong number
- The parity (odd or even) of the number 
- The sum of its digits
- A fun fact about the number ( Fetched from the Numbers API)
- Handles invalid inputs gracefullt
- Supports Cross-Origin Resource Sharing

## API Endpoint
### Request
- Method: GET
- URL: /api/classify-number?number={number}
- Example: GET/api/classify-number?number=371

### Response
Success (200 OK)

json

{

    "number": 371,
    "is_prime": false,
    "is_perfect": false,
    "properties": ["armstrong","odd"],
    "digit_sum": 11,
    "fun_fact: "371 is a narcissistic number."

}

Error ( 400 Bad Request )

json

{

    "number": "alphabet",

    "error": "true


}

### Technologies Used
- Backend: Django (Python)
- Api Doucmentation: Numbers API (http://numbersapi.com)
- CORS Handling: django-cors-headers
- Deployment [Render]

### Setup and Installation
1. Clone the Repository

``` bash
git clone https://github.com/Julzpeter/classifynumber-api.git
cd classifynumber-api
```

2. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Run MIgrations
```bash
python manage.py runserver
```

5. Run the development Server
```bash
python manage.py runserver
```

6. Access the API

Open your browser or use a tool like Postman to access

http://127.0.0.1:8000/api/classify-number?number=371

7. Testing 
To test the API, you can use tools like:
- Postman
- Curl
- Browser

Example using curl
```bash
curl "http://127.0.0.1:8000/api/classify-number?number=371"
```


