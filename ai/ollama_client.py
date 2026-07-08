import json
import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "llama3.2:latest"


def generate_ai_response(prompt):

    payload = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False
    }

    try:

        response = requests.post(
            OLLAMA_URL,
            json=payload,
            timeout=120
        )

        response.raise_for_status()

        return response.json()["response"]

    except requests.exceptions.RequestException as e:

        return f"Connection Error:\n{e}"


def explain_weather(weather_json):

    current = weather_json["current_condition"][0]

    weather_info = {
        "Temperature (°C)": current["temp_C"],
        "Humidity (%)": current["humidity"],
        "Wind Speed (km/h)": current["windspeedKmph"],
        "Description": current["weatherDesc"][0]["value"]
    }

    prompt = f"""
You are a Weather Expert.

Analyze this weather information.

{json.dumps(weather_info, indent=2)}

Provide:

1. Current weather
2. Temperature
3. Humidity
4. Wind
5. Simple recommendation.
"""

    return generate_ai_response(prompt)


def explain_currency(currency_json):

    if "rates" not in currency_json:
        return "Invalid currency data."

    important_rates = {
        "PKR": currency_json["rates"].get("PKR"),
        "USD": currency_json["rates"].get("USD"),
        "EUR": currency_json["rates"].get("EUR"),
        "GBP": currency_json["rates"].get("GBP"),
        "AED": currency_json["rates"].get("AED"),
        "SAR": currency_json["rates"].get("SAR")
    }

    prompt = f"""
You are a professional Currency Analyst.

Analyze the following exchange rates.

Base Currency:
{currency_json.get("base_code")}

Exchange Rates:
{json.dumps(important_rates, indent=2)}

Provide:

1. Base Currency
2. Explain each exchange rate briefly.
3. Overall market summary.
"""

    return generate_ai_response(prompt)


def explain_crypto(crypto_json):

    prompt = f"""
You are a Cryptocurrency Expert.

Current Prices:

{json.dumps(crypto_json, indent=2)}

Provide:

1. Bitcoin Price
2. Ethereum Price
3. Solana Price
4. Short market overview.
"""

    return generate_ai_response(prompt)