# operation

## Overview

These methods allow you to view operation details for your Neon project. For related information, see [Operations](https://neon.tech/docs/manage/operations).

### Available Operations

* [get_project_operation](#get_project_operation) - Get operation details
* [list_project_operations](#list_project_operations) - Get a list of operations

## get_project_operation

Retrieves details for the specified operation.
An operation is an action performed on a Neon project resource.
You can obtain a `project_id` by listing the projects for your Neon account.
You can obtain a `operation_id` by listing operations for the project.


### Example Usage

```python
import neon_api
from neon_api.models import operations

s = neon_api.NeonAPI(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.GetProjectOperationRequest(
    operation_id='aa52c3f5-ad01-49da-9ffe-78f097b0074f',
    project_id='dicta',
)

res = s.operation.get_project_operation(req)

if res.operation_response is not None:
    # handle response
```

## list_project_operations

Retrieves a list of operations for the specified Neon project.
You can obtain a `project_id` by listing the projects for your Neon account.
The number of operations returned can be large.
To paginate the response, issue an initial request with a `limit` value.
Then, add the `cursor` value that was returned in the response to the next request.


### Example Usage

```python
import neon_api
from neon_api.models import operations

s = neon_api.NeonAPI(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.ListProjectOperationsRequest(
    cursor='corporis',
    limit=296140,
    project_id='iusto',
)

res = s.operation.list_project_operations(req)

if res.list_project_operations_200_application_json_object is not None:
    # handle response
```
