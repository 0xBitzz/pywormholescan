from typing import Dict

import requests


def make_request(url: str, method: str="GET", timeout: int=120) -> Dict:
    try:
        response = requests.request(method, url, timeout=timeout)
        response.raise_for_status()

        content = response.json()
        return content
    except Exception as e:
        raise
