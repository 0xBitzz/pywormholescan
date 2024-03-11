from typing import Dict

import requests

from pywormholescan.internal.errors import APIRequestError


def make_request(url: str, method: str = "GET", timeout: int = 120) -> Dict:
    try:
        response = requests.request(method, url, timeout=timeout)
        response.raise_for_status()

        return response.json()
    except requests.exceptions.Timeout:
        raise APIRequestError("Timeout error occurred.")
    except requests.exceptions.ConnectionError:
        raise APIRequestError("Connection error occurred.")
    except requests.exceptions.HTTPError as e:
        raise APIRequestError(f"HTTPError: {e}")
