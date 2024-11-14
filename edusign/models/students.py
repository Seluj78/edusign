import requests

from edusign.utils import _EdusignAPI
from edusign.utils import EdusignAPIError


class Students(_EdusignAPI):
    def create(self, first_name: str, last_name: str, email_address: str) -> str:
        """
        Function to create a student in Edusign

        :param first_name:
            The first name of the student
        :param last_name:
            The last name of the student
        :param email_address:
            The email address of the student

        :return:
            A str that is the edusign DB ID of this student.
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

    def get_by_email(self, email_address: str) -> dict:
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

    def get_by_id(self, student_id: str):
        response = requests.get(
            url=f"{self.BASE_URL}/student/{student_id}",
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

    def get_all(self) -> dict:
        response = requests.get(
            url=f"{self.BASE_URL}/student",
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

    def patch(self, **kwargs) -> str:
        """
        Update a student in Edusign with given parameters.

        :param kwargs:
            The other optional student fields to update, must include at least ID, FIRSTNAME and LASTNAME

        :return:
            A message indicating success or an EdusignAPIError if there's an issue.
        """

        required_fields = ["ID", "FIRSTNAME", "LASTNAME"]
        for field in required_fields:
            if field not in kwargs:
                raise ValueError(f"The required field '{field}' is missing.")

        response = requests.patch(
            url=f"{self.BASE_URL}/student/",
            headers=self.HEADERS,
            json={
                "student": kwargs,
            },
        )

        try:
            response.raise_for_status()
        except requests.exceptions.HTTPError:
            raise EdusignAPIError(response.status_code, response.text)

        return "Student updated successfully"
