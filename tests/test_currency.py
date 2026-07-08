import json

from api.currency import get_currency_rates


base_currency = input("Enter Base Currency (Example: USD): ").upper()

currency_data = get_currency_rates(base_currency)

print("\nCurrency API Response\n")

print(json.dumps(currency_data, indent=4))