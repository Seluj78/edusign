import requests

from edusign.utils import _EdusignAPI
from edusign.utils import EdusignAPIError


class Students(_EdusignAPI):
    def create(self, first_name: str, last_name: str, email_address: str) -> int:
        """
        Function to create a student in Edusign

        :param first_name:
            The first name of the student
        :param last_name:
            The last name of the student
        :param email_address:
            The email address of the student

        :return:
            An int that is the edusign DB ID of this student.
        """
        response = requests.post(
            url=f"{self.BASE_URL}/student",
            headers=self.HEADERS,
            json={
                "student": {
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

        student_id = data["result"]["ID"]
        # TODO: Change to return all results
        return student_id

    def get_by_email(self, email_address):
        response = requests.get(
            url=f"{self.BASE_URL}/student/by-email/{email_address}",
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
