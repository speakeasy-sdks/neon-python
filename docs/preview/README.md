# preview

## Overview

New API methods that are in Beta / Preview state and could be subjected to significant changes in the future.

### Available Operations

* [list_projects_consumption](#list_projects_consumption) - Get a list of projects consumption

## list_projects_consumption

Note, this is a preview API and could be subjected to significant changes in the future.
Retrieves a list of per-project consumption for the current billing period.


### Example Usage

```python
import neon_api
from neon_api.models import operations

s = neon_api.NeonAPI(
    security=shared.Security(
        bearer_auth="YOUR_BEARER_TOKEN_HERE",
    ),
)

req = operations.ListProjectsConsumptionRequest(
    cursor='dicta',
    limit=688661,
)

res = s.preview.list_projects_consumption(req)

if res.list_projects_consumption_200_application_json_object is not None:
    # handle response
```
