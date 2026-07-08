from api.weather import get_weather
from api.currency import get_currency_rates
from api.crypto import get_crypto_prices

from ai.ollama_client import (
    explain_weather,
    explain_currency,
    explain_crypto
)

from database.db import (
    save_user_request,
    save_api_result,
    save_ai_output
)

print("\nAI Insight Vault\n")

print("1. Weather")
print("2. Currency")
print("3. Cryptocurrency")

choice = input("\nEnter Choice: ")

# -------------------------
# WEATHER
# -------------------------

if choice == "1":

    city = input("Enter City Name: ")

    request_id = save_user_request(
        "Weather",
        city
    )

    api_data = get_weather(city)

    save_api_result(
        request_id,
        "wttr.in",
        api_data
    )

    ai_response = explain_weather(api_data)

    save_ai_output(
        request_id,
        ai_response
    )

    print("\nAI Response\n")

    print(ai_response)

# -------------------------
# CURRENCY
# -------------------------

elif choice == "2":

    base = input("Enter Base Currency: ").upper()

    request_id = save_user_request(
        "Currency",
        base
    )

    api_data = get_currency_rates(base)

    save_api_result(
        request_id,
        "ExchangeRate API",
        api_data
    )

    ai_response = explain_currency(api_data)

    save_ai_output(
        request_id,
        ai_response
    )

    print("\nAI Response\n")

    print(ai_response)

# -------------------------
# CRYPTO
# -------------------------

elif choice == "3":

    request_id = save_user_request(
        "Cryptocurrency",
        "Bitcoin, Ethereum, Solana"
    )

    api_data = get_crypto_prices()

    save_api_result(
        request_id,
        "CoinGecko",
        api_data
    )

    ai_response = explain_crypto(api_data)

    save_ai_output(
        request_id,
        ai_response
    )

    print("\nAI Response\n")

    print(ai_response)

else:

    print("Invalid Choice")