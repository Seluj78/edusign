import datetime
from typing import List

import requests

from edusign.utils import _EdusignAPI
from edusign.utils import EdusignAPIError


class Courses(_EdusignAPI):
    def create(
        self,
        course_name: str,
        start_date: datetime.datetime,
        end_date: datetime.datetime,
        professor_ids: List[str],
        group_id: str,
    ):
        """
        Function to create a course in Edusign

        :param course_name:
            The name of the course being created
        :param start_date:
            The date when the course starts
        :param end_date:
            The date when the course ends
        :param professor_ids:
            List of professors in the course
        :param group_id:
            The Edusign ID of the group for this course

        :return:
            The course's ID
        """
        professors_list = {}

        for i, professor_id in enumerate(professor_ids):
            if i == 0:
                professors_list["PROFESSOR"] = professor_id
            else:
                professors_list[f"PROFESSOR_{i + 1}"] = professor_id

        course_data = {
            "course": {
                **{
                    "NAME": course_name,
                    "START": start_date,
                    "END": end_date,
                    "SCHOOL_GROUP": group_id,
                },
                **professors_list,
            }
        }

        response = requests.post(url=f"{self.BASE_URL}/course", headers=self.HEADERS, json=course_data)

        try:
            response.raise_for_status()
        except requests.exceptions.HTTPError:
            raise EdusignAPIError(response.status_code, response.text)

        data = response.json()

        if data["status"] != "success":
            raise EdusignAPIError(response.status_code, response.text)
        course_id = data["result"]["ID"]

        return course_id

    def get_by_id(self, course_id: str):
        """
        Function to get a course from their ID

        :param: course_id:
            The Edusign course's ID

        :return:
            All the data from the course
        """
        response = requests.get(
            url=f"{self.BASE_URL}/course/{course_id}",
            headers=self.HEADERS,
        )

        try:
            response.raise_for_status()
        except requests.exceptions.HTTPError:
            raise EdusignAPIError(response.status_code, response.text)

        data = response.json()

        if data["status"] != "success":
            raise EdusignAPIError(response.status_code, response.text)

        return data
