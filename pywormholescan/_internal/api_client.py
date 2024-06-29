import requests

from .network import Network
from .url_builder import build_url


class APIClient:
    def __init__(self, network: Network) -> None:
        if not isinstance(network, Network):
            raise ValueError(
                "Invalid network provided. Please use Network.MAINNET or Network.TESTNET."
            )

        self.base_url = network.value
        self.timeout = 120

    def get(self, endpoint: str) -> dict:
        url = f"{self.base_url}{endpoint}"
        try:
            response = requests.get(url, timeout=self.timeout)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"GET request failed: {e}")
            raise

    def get_with_url_builder(self, *args, **kwargs) -> dict:
        path = build_url(*args, **kwargs)
        return self.get(path)

    def post(self, endpoint: str, json: dict) -> dict:
        url = f"{self.base_url}{endpoint}"
        try:
            response = requests.post(url, json=json, timeout=self.timeout)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"POST request failed: {e}")
            raise
