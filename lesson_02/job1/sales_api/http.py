import requests

from functools import reduce
from typing import List, Dict, Any

BASE_URL = "https://fake-api-vycpfa6oca-uc.a.run.app/sales"


def fetch_data(date: str, auth_token: str) -> List[Dict[str, Any]]:
    page = 1

    result: list = []

    while page <= 4:
        response = requests.get(url=BASE_URL, params={'date': date, 'page': page},
                                headers={"Authorization": auth_token})

        if response.status_code != 200:
            break

        result.append(response.json())

        page += 1

    return reduce(lambda x, y: x + y, result)
