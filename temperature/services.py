import requests
from core.config import settings

WEATHER_API_URL = "http://api.weatherapi.com/v1/current.json"


def perform_request(city: str) -> dict:
    payload = {
        "q": city
    }
    key_api = settings.API_WEATHER_KEY
    if key_api is None:
        raise ValueError("API_WEATHER_KEY isn't set!")
    headers = {"key": key_api}
    response = requests.get(
        WEATHER_API_URL,
        params=payload,
        headers=headers
    ).json()
    return response


def parse_response(response: dict) -> float:
    temperature = response["current"]["temp_c"]

    return float(temperature)


def get_temperature(city: str) -> float:
    print(f"Performing request to Weather API for city {city}...")
    response = perform_request(city)
    temperature = parse_response(response)

    return temperature


if __name__ == "__main__":
    temperature = get_temperature("London")
    print(f"Temperature in London is {temperature} Celsius")
