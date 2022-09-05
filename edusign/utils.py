from typing import Optional

import requests


class EdusignAPIError(Exception):
    def __init__(self, status_code, message):
        self.status_code = status_code
        self.message = message

    def __str__(self):
        return repr(self)


class _EdusignAPI:
    def __init__(self, api_key: str, base_url: Optional[str] = None, test_api_key: bool = True):
        """
        Initialize the needed variables for the API

        :param api_key:
            Your Edusign API key
        :param base_url:
            The base url of the Edusign instance you're using. Defaults to "https://ext.edusign.fr/v1"
        :param test_api_key:
            Specify whether you want to test your API key or not at init. Defaults to True
        """
        self.api_key = api_key
        self.HEADERS = {"Authorization": f"Bearer {self.api_key}"}
        if base_url is None:
            self.BASE_URL = "https://ext.edusign.fr/v1"
        else:
            self.BASE_URL = base_url
        if test_api_key:
            self.test_api_key()

    def test_api_key(self):
        response = requests.get(
            url=f"{self.BASE_URL}/school",
            headers=self.HEADERS,
        )
        try:
            response.raise_for_status()
        except requests.exceptions.HTTPError:
            raise EdusignAPIError(401, "Incorrect API key.")
