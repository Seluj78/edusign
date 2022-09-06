import requests

from edusign.utils import _EdusignAPI
from edusign.utils import EdusignAPIError


class Professors(_EdusignAPI):
    def create(self, first_name: str, last_name: str, email_address: str):
        """
        Function to create a professor in Edusign

        :param first_name:
            The first name of the professor
        :param last_name:
            The last name of the professor
        :param email_address:
            The email address of the v

        :return:
            An int that is the edusign DB ID of this professor.
        """

        # TODO: Refactor student and professor creation to use a single utility function
        response = requests.post(
            url=f"{self.BASE_URL}/professor",
            headers=self.HEADERS,
            json={
                "professor": {
                    "FIRSTNAME": first_name,
                    "LASTNAME": last_name,
                    "EMAIL": email_address,
                }
            },
        )
        try:
            response.raise_for_status()
        except requests.exceptions.HTTPError:
            raise EdusignAPIError(response.status_code, response.text)

        data = response.json()

        if data["status"] != "success":
            raise EdusignAPIError(response.status_code, response.text)

        # TODO: Change to return all results
        professor_id = data["result"]["ID"]
        return professor_id

    def get_by_email(self, email_address: str) -> dict:
        """
        Get a professor based on his email address
        :param email_address:
            The email address of the professor you want to get

        :return:
            The full professor details
        """
        # TODO: Refactor student and professor get to use a single utility function
        response = requests.get(
            url=f"{self.BASE_URL}/professor/by-email/{email_address}",
            headers=self.HEADERS,
        )

        try:
            response.raise_for_status()
        except requests.exceptions.HTTPError:
            raise EdusignAPIError(response.status_code, response.text)

        data = response.json()

        if data["status"] != "success":
            raise EdusignAPIError(response.status_code, response.text)

        return data["result"]
