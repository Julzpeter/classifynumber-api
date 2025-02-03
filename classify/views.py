import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
def classify_number(request):
    ## extract number from the query parameters
    number = request.GET.get('number')

    #validate the input
    if not number or not number.lstrip('-').isdigit():
        return JsonResponse({
            "number":number if number else "null",
            "error": True
        }, status = 400)
    number = int(number)

    ## calculate properties
    is_prime= check_prime(number)
    is_perfect = check_perfect(number)
    is_armstrong = check_armstrong(number)
    parity = "odd" if number % 2 else "even"
    digit_sum = sum(int(digit)for digit in str(abs(number)))

    #determines properties list
    properties = []
    if is_armstrong:
        properties.append("armstrong")
    properties.append(parity)

    #fetch fun fact from Numbers Api

    fun_fact = get_fun_fact(number)

    #return the Json Response
    return JsonResponse({
        "number":number,
        "is_prime":is_prime,
        "is_perfect ": is_perfect,
        "properties":properties,
        "digit_sum":digit_sum,
        "fun_fact":fun_fact
    })

def check_prime(n):
    if n<2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def check_perfect(n):
    if n < 2:
        return False
    divisors = [i for i in range(1, n) if n % i == 0]
    return sum(divisors) == n

def check_armstrong(n):
    digits = [int(d)for d in str(abs(n))]
    length = len(digits)
    return sum(d**length for d in digits) == n

def get_fun_fact(n):
    url=f"http://numbersapi.com/{n}/math"
    response = requests.get(url)
    return response.text if response.status_code == 200 else "No dun fact available"