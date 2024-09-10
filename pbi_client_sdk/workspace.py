import requests  # type: ignore[import-untyped]

from .tenant import Tenant
from .utils import process_response


class Workspace:
    def __init__(self, tenant: Tenant, workspace_id: str):
        """
        Initializes the Workspace object with the required credentials.

        :param tenant:
        :param workspace_id:
        """

        self.tenant: Tenant = tenant
        self.workspace_id: str = workspace_id

    def __get_headers(self) -> dict:
        return self.tenant.access_headers

    def get_reports(self) -> list:
        """
        Fetch a list of all reports in the workspace.

        :return: Array of report objects
        """

        r = requests.get(
            f"https://api.powerbi.com/v1.0/myorg/groups/{self.workspace_id}/reports",
            headers=self.__get_headers(),
        )
        return process_response(r)

    def get_datasets(self) -> list:
        """
        Fetch a list of all datasets in the workspace.

        :return: Array of dataset objects
        """

        r = requests.get(
            f"https://api.powerbi.com/v1.0/myorg/groups/{self.workspace_id}/datasets",
            headers=self.__get_headers(),
        )
        return process_response(r)

    def get_dashboards(self) -> list:
        """
        Fetch a list of all dashboards in the workspace.

        :return: Array of dashboard objects
        """

        r = requests.get(
            f"https://api.powerbi.com/v1.0/myorg/groups/{self.workspace_id}/dashboards",
            headers=self.__get_headers(),
        )
        return process_response(r)

    def get_dataflows(self) -> list:
        """
        Fetch a list of all dataflows in the workspace.

        :return: Array of dataflow objects
        """

        r = requests.get(
            f"https://api.powerbi.com/v1.0/myorg/groups/{self.workspace_id}/dataflows",
            headers=self.__get_headers(),
        )
        return process_response(r)
