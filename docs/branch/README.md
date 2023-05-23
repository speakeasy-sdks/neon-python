# branch

## Overview

These methods allow you to create and manage branches in your Neon project. For related information, see [Manage branches](https://neon.tech/docs/manage/branches).

### Available Operations

* [create_project_branch](#create_project_branch) - Create a branch
* [create_project_branch_database](#create_project_branch_database) - Create a database
* [create_project_branch_role](#create_project_branch_role) - Create a role
* [delete_project_branch](#delete_project_branch) - Delete a branch
* [delete_project_branch_database](#delete_project_branch_database) - Delete a database
* [delete_project_branch_role](#delete_project_branch_role) - Delete a role
* [get_project_branch](#get_project_branch) - Get branch details
* [get_project_branch_database](#get_project_branch_database) - Get database details
* [get_project_branch_role](#get_project_branch_role) - Get role details
* [get_project_branch_role_password](#get_project_branch_role_password) - Get role password
* [list_project_branch_databases](#list_project_branch_databases) - Get a list of databases
* [list_project_branch_endpoints](#list_project_branch_endpoints) - Get a list of branch endpoints
* [list_project_branch_roles](#list_project_branch_roles) - Get a list of roles
* [list_project_branches](#list_project_branches) - Get a list of branches
* [reset_project_branch_role_password](#reset_project_branch_role_password) - Reset the role password
* [set_primary_project_branch](#set_primary_project_branch) - Set the branch as the primary branch of a project
* [update_project_branch](#update_project_branch) - Update a branch
* [update_project_branch_database](#update_project_branch_database) - Update a database

## create_project_branch

Creates a branch in the specified project.
You can obtain a `project_id` by listing the projects for your Neon account.

This method does not require a request body, but you can specify one to create an endpoint for the branch or to select a non-default parent branch.
The default behavior is to create a branch from the project's root branch (`main`) with no endpoint, and the branch name is auto-generated.
For related information, see [Manage branches](https://neon.tech/docs/manage/branches/).


### Example Usage

```python
import neon_api
import dateutil.parser
from neon_api.models import operations, shared

s = neon_api.NeonAPI(
    security=shared.Security(
        bearer_auth="YOUR_BEARER_TOKEN_HERE",
    ),
)

req = operations.CreateProjectBranchRequest(
    branch_create_request=shared.BranchCreateRequest(
        branch=shared.BranchCreateRequestBranch(
            name='Stuart Stiedemann',
            parent_id='vel',
            parent_lsn='error',
            parent_timestamp=dateutil.parser.isoparse('2022-03-26T09:37:56.283Z'),
        ),
        endpoints=[
            shared.BranchCreateRequestEndpointOptions(
                autoscaling_limit_max_cu=2975.34,
                autoscaling_limit_min_cu=8917.73,
                provisioner=shared.Provisioner.K8S_POD,
                suspend_timeout_seconds=963663,
                type=shared.EndpointType.READ_ONLY,
            ),
            shared.BranchCreateRequestEndpointOptions(
                autoscaling_limit_max_cu=3834.41,
                autoscaling_limit_min_cu=4776.65,
                provisioner=shared.Provisioner.K8S_NEONVM,
                suspend_timeout_seconds=812169,
                type=shared.EndpointType.READ_WRITE,
            ),
        ],
    ),
    project_id='iusto',
)

res = s.branch.create_project_branch(req)

if res.create_project_branch_201_application_json_object is not None:
    # handle response
```

## create_project_branch_database

Creates a database in the specified branch.
A branch can have multiple databases.
You can obtain a `project_id` by listing the projects for your Neon account.
You can obtain the `branch_id` by listing the project's branches.
For related information, see [Manage databases](https://neon.tech/docs/manage/databases/).


### Example Usage

```python
import neon_api
from neon_api.models import operations, shared

s = neon_api.NeonAPI(
    security=shared.Security(
        bearer_auth="YOUR_BEARER_TOKEN_HERE",
    ),
)

req = operations.CreateProjectBranchDatabaseRequest(
    database_create_request=shared.DatabaseCreateRequest(
        database=shared.DatabaseCreateRequestDatabase(
            name='Charlie Walsh II',
            owner_name='veritatis',
        ),
    ),
    branch_id='deserunt',
    project_id='perferendis',
)

res = s.branch.create_project_branch_database(req)

if res.database_operations is not None:
    # handle response
```

## create_project_branch_role

Creates a role in the specified branch.
You can obtain a `project_id` by listing the projects for your Neon account.
You can obtain the `branch_id` by listing the project's branches.
In Neon, the terms "role" and "user" are synonymous.
For related information, see [Manage users](https://neon.tech/docs/manage/users/).

Connections established to the active read-write endpoint will be dropped.
If the read-write endpoint is idle, the endpoint becomes active for a short period of time and is suspended afterward.


### Example Usage

```python
import neon_api
from neon_api.models import operations, shared

s = neon_api.NeonAPI(
    security=shared.Security(
        bearer_auth="YOUR_BEARER_TOKEN_HERE",
    ),
)

req = operations.CreateProjectBranchRoleRequest(
    role_create_request=shared.RoleCreateRequest(
        role=shared.RoleCreateRequestRole(
            name='Estelle Will',
        ),
    ),
    branch_id='at',
    project_id='at',
)

res = s.branch.create_project_branch_role(req)

if res.role_operations is not None:
    # handle response
```

## delete_project_branch

Deletes the specified branch from a project, and places
all endpoints into an idle state, breaking existing client connections.
You can obtain a `project_id` by listing the projects for your Neon account.
You can obtain a `branch_id` by listing the project's branches.
For related information, see [Manage branches](https://neon.tech/docs/manage/branches/).

When a successful response status is received, the endpoints are still active,
and the branch is not yet deleted from storage.
The deletion occurs after all operations finish.
You cannot delete a branch if it is the only remaining branch in the project.
A project must have at least one branch.


### Example Usage

```python
import neon_api
from neon_api.models import operations

s = neon_api.NeonAPI(
    security=shared.Security(
        bearer_auth="YOUR_BEARER_TOKEN_HERE",
    ),
)

req = operations.DeleteProjectBranchRequest(
    branch_id='maiores',
    project_id='molestiae',
)

res = s.branch.delete_project_branch(req)

if res.branch_operations is not None:
    # handle response
```

## delete_project_branch_database

Deletes the specified database from the branch.
You can obtain a `project_id` by listing the projects for your Neon account.
You can obtain the `branch_id` and `database_name` by listing branch's databases.
For related information, see [Manage databases](https://neon.tech/docs/manage/databases/).


### Example Usage

```python
import neon_api
from neon_api.models import operations

s = neon_api.NeonAPI(
    security=shared.Security(
        bearer_auth="YOUR_BEARER_TOKEN_HERE",
    ),
)

req = operations.DeleteProjectBranchDatabaseRequest(
    branch_id='quod',
    database_name='quod',
    project_id='esse',
)

res = s.branch.delete_project_branch_database(req)

if res.database_operations is not None:
    # handle response
```

## delete_project_branch_role

Deletes the specified role from the branch.
You can obtain a `project_id` by listing the projects for your Neon account.
You can obtain the `branch_id` by listing the project's branches.
You can obtain the `role_name` by listing the roles for a branch.
In Neon, the terms "role" and "user" are synonymous.
For related information, see [Managing users](https://neon.tech/docs/manage/users/).


### Example Usage

```python
import neon_api
from neon_api.models import operations

s = neon_api.NeonAPI(
    security=shared.Security(
        bearer_auth="YOUR_BEARER_TOKEN_HERE",
    ),
)

req = operations.DeleteProjectBranchRoleRequest(
    branch_id='totam',
    project_id='porro',
    role_name='dolorum',
)

res = s.branch.delete_project_branch_role(req)

if res.role_operations is not None:
    # handle response
```

## get_project_branch

Retrieves information about the specified branch.
You can obtain a `project_id` by listing the projects for your Neon account.
You can obtain a `branch_id` by listing the project's branches.
A `branch_id` value has a `br-` prefix.

Each Neon project has a root branch named `main`.
A project may contain child branches that were branched from `main` or from another branch.
A parent branch is identified by a `parent_id` value, which is the `id` of the parent branch.
For related information, see [Manage branches](https://neon.tech/docs/manage/branches/).


### Example Usage

```python
import neon_api
from neon_api.models import operations

s = neon_api.NeonAPI(
    security=shared.Security(
        bearer_auth="YOUR_BEARER_TOKEN_HERE",
    ),
)

req = operations.GetProjectBranchRequest(
    branch_id='dicta',
    project_id='nam',
)

res = s.branch.get_project_branch(req)

if res.branch_response is not None:
    # handle response
```

## get_project_branch_database

Retrieves information about the specified database.
You can obtain a `project_id` by listing the projects for your Neon account.
You can obtain the `branch_id` and `database_name` by listing branch's databases.
For related information, see [Manage databases](https://neon.tech/docs/manage/databases/).


### Example Usage

```python
import neon_api
from neon_api.models import operations

s = neon_api.NeonAPI(
    security=shared.Security(
        bearer_auth="YOUR_BEARER_TOKEN_HERE",
    ),
)

req = operations.GetProjectBranchDatabaseRequest(
    branch_id='officia',
    database_name='occaecati',
    project_id='fugit',
)

res = s.branch.get_project_branch_database(req)

if res.database_response is not None:
    # handle response
```

## get_project_branch_role

Retrieves details about the specified role.
You can obtain a `project_id` by listing the projects for your Neon account.
You can obtain the `branch_id` by listing the project's branches.
You can obtain the `role_name` by listing the roles for a branch.
In Neon, the terms "role" and "user" are synonymous.
For related information, see [Managing users](https://neon.tech/docs/manage/users/).


### Example Usage

```python
import neon_api
from neon_api.models import operations

s = neon_api.NeonAPI(
    security=shared.Security(
        bearer_auth="YOUR_BEARER_TOKEN_HERE",
    ),
)

req = operations.GetProjectBranchRoleRequest(
    branch_id='deleniti',
    project_id='hic',
    role_name='optio',
)

res = s.branch.get_project_branch_role(req)

if res.role_response is not None:
    # handle response
```

## get_project_branch_role_password

Retrieves password of the specified role if possible.
You can obtain a `project_id` by listing the projects for your Neon account.
You can obtain the `branch_id` by listing the project's branches.
You can obtain the `role_name` by listing the roles for a branch.
In Neon, the terms "role" and "user" are synonymous.
For related information, see [Managing users](https://neon.tech/docs/manage/users/).


### Example Usage

```python
import neon_api
from neon_api.models import operations

s = neon_api.NeonAPI(
    security=shared.Security(
        bearer_auth="YOUR_BEARER_TOKEN_HERE",
    ),
)

req = operations.GetProjectBranchRolePasswordRequest(
    branch_id='totam',
    project_id='beatae',
    role_name='commodi',
)

res = s.branch.get_project_branch_role_password(req)

if res.role_password_response is not None:
    # handle response
```

## list_project_branch_databases

Retrieves a list of databases for the specified branch.
A branch can have multiple databases.
You can obtain a `project_id` by listing the projects for your Neon account.
You can obtain the `branch_id` by listing the project's branches.
For related information, see [Manage databases](https://neon.tech/docs/manage/databases/).


### Example Usage

```python
import neon_api
from neon_api.models import operations

s = neon_api.NeonAPI(
    security=shared.Security(
        bearer_auth="YOUR_BEARER_TOKEN_HERE",
    ),
)

req = operations.ListProjectBranchDatabasesRequest(
    branch_id='molestiae',
    project_id='modi',
)

res = s.branch.list_project_branch_databases(req)

if res.databases_response is not None:
    # handle response
```

## list_project_branch_endpoints

Retrieves a list of endpoints for the specified branch.
Currently, Neon permits only one endpoint per branch.
You can obtain a `project_id` by listing the projects for your Neon account.
You can obtain the `branch_id` by listing the project's branches.


### Example Usage

```python
import neon_api
from neon_api.models import operations

s = neon_api.NeonAPI(
    security=shared.Security(
        bearer_auth="YOUR_BEARER_TOKEN_HERE",
    ),
)

req = operations.ListProjectBranchEndpointsRequest(
    branch_id='qui',
    project_id='impedit',
)

res = s.branch.list_project_branch_endpoints(req)

if res.endpoints_response is not None:
    # handle response
```

## list_project_branch_roles

Retrieves a list of roles from the specified branch.
You can obtain a `project_id` by listing the projects for your Neon account.
You can obtain the `branch_id` by listing the project's branches.
In Neon, the terms "role" and "user" are synonymous.
For related information, see [Manage users](https://neon.tech/docs/manage/users/).


### Example Usage

```python
import neon_api
from neon_api.models import operations

s = neon_api.NeonAPI(
    security=shared.Security(
        bearer_auth="YOUR_BEARER_TOKEN_HERE",
    ),
)

req = operations.ListProjectBranchRolesRequest(
    branch_id='cum',
    project_id='esse',
)

res = s.branch.list_project_branch_roles(req)

if res.roles_response is not None:
    # handle response
```

## list_project_branches

Retrieves a list of branches for the specified project.
You can obtain a `project_id` by listing the projects for your Neon account.

Each Neon project has a root branch named `main`.
A `branch_id` value has a `br-` prefix.
A project may contain child branches that were branched from `main` or from another branch.
A parent branch is identified by the `parent_id` value, which is the `id` of the parent branch.
For related information, see [Manage branches](https://neon.tech/docs/manage/branches/).


### Example Usage

```python
import neon_api
from neon_api.models import operations

s = neon_api.NeonAPI(
    security=shared.Security(
        bearer_auth="YOUR_BEARER_TOKEN_HERE",
    ),
)

req = operations.ListProjectBranchesRequest(
    project_id='ipsum',
)

res = s.branch.list_project_branches(req)

if res.branches_response is not None:
    # handle response
```

## reset_project_branch_role_password

Resets the password for the specified role.
Returns a new password and operations. The new password is ready to use when the last operation finishes.
The old password remains valid until last operation finishes.
Connections to the read-write endpoint are dropped. If idle,
the read-write endpoint becomes active for a short period of time.

You can obtain a `project_id` by listing the projects for your Neon account.
You can obtain the `branch_id` by listing the project's branches.
You can obtain the `role_name` by listing the roles for a branch.
In Neon, the terms "role" and "user" are synonymous.
For related information, see [Managing users](https://neon.tech/docs/manage/users/).


### Example Usage

```python
import neon_api
from neon_api.models import operations

s = neon_api.NeonAPI(
    security=shared.Security(
        bearer_auth="YOUR_BEARER_TOKEN_HERE",
    ),
)

req = operations.ResetProjectBranchRolePasswordRequest(
    branch_id='excepturi',
    project_id='aspernatur',
    role_name='perferendis',
)

res = s.branch.reset_project_branch_role_password(req)

if res.role_operations is not None:
    # handle response
```

## set_primary_project_branch

The primary mark is automatically removed from the previous primary branch.
You can obtain a `project_id` by listing the projects for your Neon account.
You can obtain the `branch_id` by listing the project's branches.
For more information, see [Manage branches](https://neon.tech/docs/manage/branches/).


### Example Usage

```python
import neon_api
from neon_api.models import operations

s = neon_api.NeonAPI(
    security=shared.Security(
        bearer_auth="YOUR_BEARER_TOKEN_HERE",
    ),
)

req = operations.SetPrimaryProjectBranchRequest(
    branch_id='ad',
    project_id='natus',
)

res = s.branch.set_primary_project_branch(req)

if res.branch_operations is not None:
    # handle response
```

## update_project_branch

Updates the specified branch. Only changing the branch name is supported.
You can obtain a `project_id` by listing the projects for your Neon account.
You can obtain the `branch_id` by listing the project's branches.
For more information, see [Manage branches](https://neon.tech/docs/manage/branches/).


### Example Usage

```python
import neon_api
from neon_api.models import operations, shared

s = neon_api.NeonAPI(
    security=shared.Security(
        bearer_auth="YOUR_BEARER_TOKEN_HERE",
    ),
)

req = operations.UpdateProjectBranchRequest(
    branch_update_request=shared.BranchUpdateRequest(
        branch=shared.BranchUpdateRequestBranch(
            name='Sheryl Fadel',
        ),
    ),
    branch_id='hic',
    project_id='saepe',
)

res = s.branch.update_project_branch(req)

if res.branch_operations is not None:
    # handle response
```

## update_project_branch_database

Updates the specified database in the branch.
You can obtain a `project_id` by listing the projects for your Neon account.
You can obtain the `branch_id` and `database_name` by listing the branch's databases.
For related information, see [Manage databases](https://neon.tech/docs/manage/databases/).


### Example Usage

```python
import neon_api
from neon_api.models import operations, shared

s = neon_api.NeonAPI(
    security=shared.Security(
        bearer_auth="YOUR_BEARER_TOKEN_HERE",
    ),
)

req = operations.UpdateProjectBranchDatabaseRequest(
    database_update_request=shared.DatabaseUpdateRequest(
        database=shared.DatabaseUpdateRequestDatabase(
            name='Harvey Hessel',
            owner_name='saepe',
        ),
    ),
    branch_id='quidem',
    database_name='architecto',
    project_id='ipsa',
)

res = s.branch.update_project_branch_database(req)

if res.database_operations is not None:
    # handle response
```
