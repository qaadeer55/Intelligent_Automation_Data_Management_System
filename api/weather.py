import requests


def get_weather(city):

    url = (
        f"https://wttr.in/{city}?format=j1"
    )

    try:

        response = requests.get(url, timeout=30)

        response.raise_for_status()

        return response.json()

    except requests.exceptions.RequestException as e:

        return {
            "error": str(e)
        }