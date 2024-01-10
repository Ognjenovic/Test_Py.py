# Python Script with Open Source Vulnerability

# Open Source Vulnerability: Using an outdated version of a widely used library
import requests  # Using an outdated version of the requests library

def fetch_data(url):
    response = requests.get(url, verify=True)  # Ignore SSL/TLS certificate verification for demonstration purposes
    return response.text

# Vulnerability 2: Not handling user input properly
def divide_numbers():
    try:
        num1 = float(input("Enter the numerator: "))
        num2 = float(input("Enter the denominator: "))
        result = num1 / num2
        print(f"The result of the division is: {result}")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except ValueError:
        print("Error: Invalid input. Please enter valid numbers.")

# New Vulnerability: Insecure password storage
def authenticate_user(username, password):
    stored_password = "hardcoded_password"  # Insecure password storage
    if password == stored_password:
        print(f"Authentication successful for user: {username}")
    else:
        print("Authentication failed.")

# Open Source Vulnerability: Using an outdated version of a widely used library
def make_api_request():
    response = requests.get("https://example-api.com", timeout=5)  # Outdated version with potential security issues
    print(f"API response: {response.text}")

# Call the functions with open source vulnerabilities
url = "https://example.com/api/data"
data = fetch_data(url)

divide_numbers()

username = input("Enter your username: ")
password = input("Enter your password: ")
authenticate_user(username, password)

make_api_request()
