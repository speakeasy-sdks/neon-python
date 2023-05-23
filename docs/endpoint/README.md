# endpoint

## Overview

These methods allow you to create and manage compute endpoints in your Neon project. For related information, see [Manage compute endpoints](https://neon.tech/docs/manage/endpoints).

### Available Operations

* [create_project_endpoint](#create_project_endpoint) - Create an endpoint
* [delete_project_endpoint](#delete_project_endpoint) - Delete an endpoint
* [get_project_endpoint](#get_project_endpoint) - Get an endpoint
* [list_project_endpoints](#list_project_endpoints) - Get a list of endpoints
* [start_project_endpoint](#start_project_endpoint) - Start an endpoint
* [suspend_project_endpoint](#suspend_project_endpoint) - Suspend an endpoint
* [update_project_endpoint](#update_project_endpoint) - Update an endpoint

## create_project_endpoint

Creates an endpoint for the specified branch.
An endpoint is a Neon compute instance.
There is a maximum of one endpoint per branch.
If the specified branch already has an endpoint, the operation fails.

You can obtain a `project_id` by listing the projects for your Neon account.
You can obtain `branch_id` by listing the project's branches.
A `branch_id` has a `br-` prefix.
Currently, only the `read_write` endpoint type is supported.
For supported regions and `region_id` values, see [Regions](https://neon.tech/docs/introduction/regions/).
For more information about endpoints, see [Manage endpoints](https://neon.tech/docs/manage/endpoints/).


### Example Usage

```python
import neon_api
from neon_api.models import operations, shared

s = neon_api.NeonAPI(
    security=shared.Security(
        bearer_auth="YOUR_BEARER_TOKEN_HERE",
    ),
)

req = operations.CreateProjectEndpointRequest(
    endpoint_create_request=shared.EndpointCreateRequest(
        endpoint=shared.EndpointCreateRequestEndpoint(
            autoscaling_limit_max_cu=9698.1,
            autoscaling_limit_min_cu=6667.67,
            branch_id='mollitia',
            disabled=False,
            passwordless_access=False,
            pooler_enabled=False,
            pooler_mode=shared.EndpointPoolerMode.TRANSACTION,
            provisioner=shared.Provisioner.K8S_NEONVM,
            region_id='dolores',
            settings=shared.EndpointSettingsData(
                pg_settings={
                    "corporis": 'explicabo',
                },
            ),
            suspend_timeout_seconds=750686,
            type=shared.EndpointType.READ_ONLY,
        ),
    ),
    project_id='omnis',
)

res = s.endpoint.create_project_endpoint(req)

if res.endpoint_operations is not None:
    # handle response
```

## delete_project_endpoint

Delete the specified endpoint.
An endpoint is a Neon compute instance.
Deleting an endpoint drops existing network connections to the endpoint.
The deletion is completed when last operation in the chain finishes successfully.

You can obtain a `project_id` by listing the projects for your Neon account.
You can obtain an `endpoint_id` by listing your project's endpoints.
An `endpoint_id` has an `ep-` prefix.
For more information about endpoints, see [Manage endpoints](https://neon.tech/docs/manage/endpoints/).


### Example Usage

```python
import neon_api
from neon_api.models import operations

s = neon_api.NeonAPI(
    security=shared.Security(
        bearer_auth="YOUR_BEARER_TOKEN_HERE",
    ),
)

req = operations.DeleteProjectEndpointRequest(
    endpoint_id='nemo',
    project_id='minima',
)

res = s.endpoint.delete_project_endpoint(req)

if res.endpoint_operations is not None:
    # handle response
```

## get_project_endpoint

Retrieves information about the specified endpoint.
An endpoint is a Neon compute instance.
You can obtain a `project_id` by listing the projects for your Neon account.
You can obtain an `endpoint_id` by listing your project's endpoints.
An `endpoint_id` has an `ep-` prefix.
For more information about endpoints, see [Manage endpoints](https://neon.tech/docs/manage/endpoints/).


### Example Usage

```python
import neon_api
from neon_api.models import operations

s = neon_api.NeonAPI(
    security=shared.Security(
        bearer_auth="YOUR_BEARER_TOKEN_HERE",
    ),
)

req = operations.GetProjectEndpointRequest(
    endpoint_id='excepturi',
    project_id='accusantium',
)

res = s.endpoint.get_project_endpoint(req)

if res.endpoint_response is not None:
    # handle response
```

## list_project_endpoints

Retrieves a list of endpoints for the specified project.
An endpoint is a Neon compute instance.
You can obtain a `project_id` by listing the projects for your Neon account.
For more information about endpoints, see [Manage endpoints](https://neon.tech/docs/manage/endpoints/).


### Example Usage

```python
import neon_api
from neon_api.models import operations

s = neon_api.NeonAPI(
    security=shared.Security(
        bearer_auth="YOUR_BEARER_TOKEN_HERE",
    ),
)

req = operations.ListProjectEndpointsRequest(
    project_id='iure',
)

res = s.endpoint.list_project_endpoints(req)

if res.endpoints_response is not None:
    # handle response
```

## start_project_endpoint

Starts an endpoint. The endpoint is ready to use
after the last operation in chain finishes successfully.

You can obtain a `project_id` by listing the projects for your Neon account.
You can obtain an `endpoint_id` by listing your project's endpoints.
An `endpoint_id` has an `ep-` prefix.
For more information about endpoints, see [Manage endpoints](https://neon.tech/docs/manage/endpoints/).


### Example Usage

```python
import neon_api
from neon_api.models import operations

s = neon_api.NeonAPI(
    security=shared.Security(
        bearer_auth="YOUR_BEARER_TOKEN_HERE",
    ),
)

req = operations.StartProjectEndpointRequest(
    endpoint_id='culpa',
    project_id='doloribus',
)

res = s.endpoint.start_project_endpoint(req)

if res.endpoint_operations is not None:
    # handle response
```

## suspend_project_endpoint

Suspend the specified endpoint
You can obtain a `project_id` by listing the projects for your Neon account.
You can obtain an `endpoint_id` by listing your project's endpoints.
An `endpoint_id` has an `ep-` prefix.
For more information about endpoints, see [Manage endpoints](https://neon.tech/docs/manage/endpoints/).


### Example Usage

```python
import neon_api
from neon_api.models import operations

s = neon_api.NeonAPI(
    security=shared.Security(
        bearer_auth="YOUR_BEARER_TOKEN_HERE",
    ),
)

req = operations.SuspendProjectEndpointRequest(
    endpoint_id='sapiente',
    project_id='architecto',
)

res = s.endpoint.suspend_project_endpoint(req)

if res.endpoint_operations is not None:
    # handle response
```

## update_project_endpoint

Updates the specified endpoint. Currently, only changing the associated branch is supported.
The branch that you specify cannot have an existing endpoint.

You can obtain a `project_id` by listing the projects for your Neon account.
You can obtain an `endpoint_id` and `branch_id` by listing your project's endpoints.
An `endpoint_id` has an `ep-` prefix. A `branch_id` has a `br-` prefix.
For more information about endpoints, see [Manage endpoints](https://neon.tech/docs/manage/endpoints/).

If the returned list of operations is not empty, the endpoint is not ready to use.
The client must wait for the last operation to finish before using the endpoint.
If the endpoint was idle before the update, the endpoint becomes active for a short period of time,
and the control plane suspends it again after the update.


### Example Usage

```python
import neon_api
from neon_api.models import operations, shared

s = neon_api.NeonAPI(
    security=shared.Security(
        bearer_auth="YOUR_BEARER_TOKEN_HERE",
    ),
)

req = operations.UpdateProjectEndpointRequest(
    endpoint_update_request=shared.EndpointUpdateRequest(
        endpoint=shared.EndpointUpdateRequestEndpoint(
            autoscaling_limit_max_cu=6527.9,
            autoscaling_limit_min_cu=2088.76,
            branch_id='culpa',
            disabled=False,
            passwordless_access=False,
            pooler_enabled=False,
            pooler_mode=shared.EndpointPoolerMode.TRANSACTION,
            provisioner=shared.Provisioner.K8S_POD,
            settings=shared.EndpointSettingsData(
                pg_settings={
                    "mollitia": 'occaecati',
                    "numquam": 'commodi',
                    "quam": 'molestiae',
                    "velit": 'error',
                },
            ),
            suspend_timeout_seconds=158969,
        ),
    ),
    endpoint_id='quis',
    project_id='vitae',
)

res = s.endpoint.update_project_endpoint(req)

if res.endpoint_operations is not None:
    # handle response
```
