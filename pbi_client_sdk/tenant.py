import requests  # type: ignore[import-untyped]
from datetime import datetime, timedelta

from .const import MS_OAUTH_URL, MS_OAUTH_SCOPE
from .utils import process_response


class Tenant:
    def __init__(self, tenant_id: str, client_id: str, client_secret: str):
        """
        Initializes the Tenant object with the required credentials.

        :param tenant_id:
        :param client_id:
        :param client_secret:
        """

        self.tenant_id: str = tenant_id
        self.client_id: str = client_id
        self.client_secret: str = client_secret

        self.__token = None
        self.__token_expiry = None
        self.__token = self.token

    @property
    def token(self) -> str:
        if not self.__token or self.__token_expiry < datetime.now():  # type: ignore[operator]
            return self.__refresh_token()

        return self.__token

    @property
    def access_headers(self) -> dict:
        return {"Authorization": f"Bearer {self.token}"}

    def __refresh_token(self):
        """Refresh the token using the provided credentials."""

        payload = {
            "grant_type": "client_credentials",
            "scope": MS_OAUTH_SCOPE,
            "client_id": self.client_id,
            "client_secret": self.client_secret,
        }
        r = requests.post(MS_OAUTH_URL.format(id=self.tenant_id), payload)
        ans = process_response(r)

        self.__token = ans["access_token"]
        self.__token_expiry = datetime.now() + timedelta(seconds=ans["expires_in"] // 2)

        return self.__token

    def list_workspaces(self) -> list[str]:
        """
        Fetch a list of all workspaces that the user has access to.

        :return: Array of workspace_id
        """

        r = requests.get(
            "https://api.powerbi.com/v1.0/myorg/groups", headers=self.access_headers
        )
        ans = process_response(r)

        return [w.get("id") for w in ans["value"]]
