import requests


def get_currency_rates(base_currency="USD"):

    url = f"https://open.er-api.com/v6/latest/{base_currency}"

    try:

        response = requests.get(url, timeout=30)

        response.raise_for_status()

        return response.json()

    except requests.exceptions.RequestException as e:

        return {
            "error": str(e)
        }