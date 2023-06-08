# neon-api

<!-- Start SDK Installation -->
## SDK Installation

```bash
pip install git+https://github.com/speakeasy-sdks/neon-python.git
```
<!-- End SDK Installation -->

## SDK Example Usage
<!-- Start SDK Example Usage -->
```python
import neon_api
from neon_api.models import shared

s = neon_api.NeonAPI(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = shared.APIKeyCreateRequest(
    key_name='corrupti',
)

res = s.api_key.create_api_key(req)

if res.api_key_create_response is not None:
    # handle response
```
<!-- End SDK Example Usage -->

<!-- Start SDK Available Operations -->
## Available Resources and Operations


### [api_key](docs/apikey/README.md)

* [create_api_key](docs/apikey/README.md#create_api_key) - Create an API key
* [list_api_keys](docs/apikey/README.md#list_api_keys) - Get a list of API keys
* [revoke_api_key](docs/apikey/README.md#revoke_api_key) - Revoke an API key

### [branch](docs/branch/README.md)

* [create_project_branch](docs/branch/README.md#create_project_branch) - Create a branch
* [create_project_branch_database](docs/branch/README.md#create_project_branch_database) - Create a database
* [create_project_branch_role](docs/branch/README.md#create_project_branch_role) - Create a role
* [delete_project_branch](docs/branch/README.md#delete_project_branch) - Delete a branch
* [delete_project_branch_database](docs/branch/README.md#delete_project_branch_database) - Delete a database
* [delete_project_branch_role](docs/branch/README.md#delete_project_branch_role) - Delete a role
* [get_project_branch](docs/branch/README.md#get_project_branch) - Get branch details
* [get_project_branch_database](docs/branch/README.md#get_project_branch_database) - Get database details
* [get_project_branch_role](docs/branch/README.md#get_project_branch_role) - Get role details
* [get_project_branch_role_password](docs/branch/README.md#get_project_branch_role_password) - Get role password
* [list_project_branch_databases](docs/branch/README.md#list_project_branch_databases) - Get a list of databases
* [list_project_branch_endpoints](docs/branch/README.md#list_project_branch_endpoints) - Get a list of branch endpoints
* [list_project_branch_roles](docs/branch/README.md#list_project_branch_roles) - Get a list of roles
* [list_project_branches](docs/branch/README.md#list_project_branches) - Get a list of branches
* [reset_project_branch_role_password](docs/branch/README.md#reset_project_branch_role_password) - Reset the role password
* [set_primary_project_branch](docs/branch/README.md#set_primary_project_branch) - Set the branch as the primary branch of a project
* [update_project_branch](docs/branch/README.md#update_project_branch) - Update a branch
* [update_project_branch_database](docs/branch/README.md#update_project_branch_database) - Update a database

### [endpoint](docs/endpoint/README.md)

* [create_project_endpoint](docs/endpoint/README.md#create_project_endpoint) - Create an endpoint
* [delete_project_endpoint](docs/endpoint/README.md#delete_project_endpoint) - Delete an endpoint
* [get_project_endpoint](docs/endpoint/README.md#get_project_endpoint) - Get an endpoint
* [list_project_endpoints](docs/endpoint/README.md#list_project_endpoints) - Get a list of endpoints
* [start_project_endpoint](docs/endpoint/README.md#start_project_endpoint) - Start an endpoint
* [suspend_project_endpoint](docs/endpoint/README.md#suspend_project_endpoint) - Suspend an endpoint
* [update_project_endpoint](docs/endpoint/README.md#update_project_endpoint) - Update an endpoint

### [operation](docs/operation/README.md)

* [get_project_operation](docs/operation/README.md#get_project_operation) - Get operation details
* [list_project_operations](docs/operation/README.md#list_project_operations) - Get a list of operations

### [preview](docs/preview/README.md)

* [list_projects_consumption](docs/preview/README.md#list_projects_consumption) - Get a list of projects consumption

### [project](docs/project/README.md)

* [create_project](docs/project/README.md#create_project) - Create a project
* [delete_project](docs/project/README.md#delete_project) - Delete a project
* [get_project](docs/project/README.md#get_project) - Get project details
* [list_projects](docs/project/README.md#list_projects) - Get a list of projects
* [update_project](docs/project/README.md#update_project) - Update a project
<!-- End SDK Available Operations -->

### Maturity

This SDK is in beta, and there may be breaking changes between versions without a major version update. Therefore, we recommend pinning usage
to a specific package version. This way, you can install the same version each time without breaking changes unless you are intentionally
looking for the latest version.

### Contributions

While we value open-source contributions to this SDK, this library is generated programmatically.
Feel free to open a PR or a Github issue as a proof of concept and we'll do our best to include it in a future release !

### SDK Created by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
