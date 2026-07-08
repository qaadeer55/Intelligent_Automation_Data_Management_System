from api.weather import get_weather
from api.currency import get_currency_rates
from api.crypto import get_crypto_prices

from ai.ollama_client import (
    explain_weather,
    explain_currency,
    explain_crypto
)

print("Select Service")
print("1. Weather")
print("2. Currency")
print("3. Cryptocurrency")

choice = input("\nEnter Choice: ")

if choice == "1":

    city = input("Enter City Name: ")

    weather = get_weather(city)

    response = explain_weather(weather)

    print("\nAI Explanation\n")

    print(response)

elif choice == "2":

    base = input("Enter Base Currency: ").upper()

    currency = get_currency_rates(base)

    response = explain_currency(currency)

    print("\nAI Explanation\n")

    print(response)

elif choice == "3":

    crypto = get_crypto_prices()

    response = explain_crypto(crypto)

    print("\nAI Explanation\n")

    print(response)

else:

    print("Invalid Choice")