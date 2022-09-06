from typing import List

import requests

from edusign.utils import _EdusignAPI
from edusign.utils import EdusignAPIError


class Groups(_EdusignAPI):
    def create(self, group_name: str, student_list: List[str]):
        """
        Create a group inside Edusign

        :param group_name:
            The name of the groupe being created.
        :param student_list:
            The list of edusign IDs that will be in the group
        :return:
            The group's ID
        """
        response = requests.post(
            url=f"{self.BASE_URL}/group",
            headers=self.HEADERS,
            json={"group": {"NAME": group_name, "STUDENTS": student_list}},
        )
        try:
            response.raise_for_status()
        except requests.exceptions.HTTPError:
            raise EdusignAPIError(response.status_code, response.text)

        data = response.json()

        if data["status"] != "success":
            raise EdusignAPIError(response.status_code, response.text)

        group_id = data["result"]["ID"]

        return group_id
