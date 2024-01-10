# Vulnerable Python Script

# Vulnerability 1: Using an outdated library
import requests  # This may have vulnerabilities if not updated

def fetch_data(url):
    response = requests.get(url)
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

# Call the vulnerable functions
url = "https://example.com/api/data"
data = fetch_data(url)

divide_numbers()
