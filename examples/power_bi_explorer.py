import os

from pbi_client_sdk.tenant import Tenant
from pbi_client_sdk.workspace import Workspace


tenant = Tenant(
    tenant_id=os.getenv("AZURE_TENANT_ID"),
    client_id=os.getenv("AZURE_CLIENT_ID"),
    client_secret=os.getenv("AZURE_CLIENT_SECRET")
)

workspace = Workspace(tenant, "test-workspace")
print(workspace.get_datasets())
print(workspace.get_reports())
print(tenant.list_workspaces())
