from typing import Any

from logzero import logger
import requests as requests


class Client:
    def __init__(self, search_parameters: dict[str, str], url_suffix: str):
        self.url = f"https://api.pushshift.io/{url_suffix}"
        self.get_request_parameters = search_parameters

    def set_request_parameter(self, key: str, value: Any):
        self.get_request_parameters[key] = value

    def search(self) -> dict[str, Any]:
        logger.info(f"Making api GET request: {self.url}")
        response = requests.get(
            self.url,
            params=self.get_request_parameters,
        )

        if response.status_code == 200:
            logger.info(f"Search results are successfully received")
            return response.json()
        else:
            logger.info(f"Error while getting search results from API: {response.status_code}, {response.text}")
            raise Exception("Unable to get search results from API")
