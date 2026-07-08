import json

from api.crypto import get_crypto_prices


crypto_data = get_crypto_prices()

print("\nCryptocurrency API Response\n")

print(json.dumps(crypto_data, indent=4))