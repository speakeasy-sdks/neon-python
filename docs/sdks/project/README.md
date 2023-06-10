# project

## Overview

These methods allow you to create and manage Neon projects. For related information, see [Manage projects](https://neon.tech/docs/manage/projects).

### Available Operations

* [create_project](#create_project) - Create a project
* [delete_project](#delete_project) - Delete a project
* [get_project](#get_project) - Get project details
* [list_projects](#list_projects) - Get a list of projects
* [update_project](#update_project) - Update a project

## create_project

Creates a Neon project.
A project is the top-level object in the Neon object hierarchy.
Plan limits define how many projects you can create.
Neon's Free plan permits one project per Neon account.
For more information, see [Manage projects](https://neon.tech/docs/manage/projects/).

You can specify a region and PostgreSQL version in the request body.
Neon currently supports PostgreSQL 14 and 15.
For supported regions and `region_id` values, see [Regions](https://neon.tech/docs/introduction/regions/).


### Example Usage

```python
import neon_api
from neon_api.models import shared

s = neon_api.NeonAPI(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = shared.ProjectCreateRequest(
    project=shared.ProjectCreateRequestProject(
        autoscaling_limit_max_cu=3179.83,
        autoscaling_limit_min_cu=8804.76,
        branch=shared.ProjectCreateRequestProjectBranch(
            database_name='commodi',
            name='Eric Emmerich',
            role_name='excepturi',
        ),
        default_endpoint_settings={
            "modi": 'praesentium',
            "rem": 'voluptates',
            "quasi": 'repudiandae',
            "sint": 'veritatis',
        },
        name='Miss Randall Hamill',
        pg_version=131797,
        provisioner=shared.Provisioner.K8S_NEONVM,
        region_id='distinctio',
        settings=shared.ProjectSettingsData(
            quota=shared.ProjectQuota(
                active_time_seconds=841386,
                compute_time_seconds=289406,
                data_transfer_bytes=264730,
                logical_size_bytes=183191,
                written_data_bytes=397821,
            ),
        ),
        store_passwords=False,
    ),
)

res = s.project.create_project(req)

if res.create_project_201_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `request`                                                                  | [shared.ProjectCreateRequest](../../models/shared/projectcreaterequest.md) | :heavy_check_mark:                                                         | The request object to use for the request.                                 |


### Response

**[operations.CreateProjectResponse](../../models/operations/createprojectresponse.md)**


## delete_project

Deletes the specified project.
You can obtain a `project_id` by listing the projects for your Neon account.
Deleting a project is a permanent action.
Deleting a project also deletes endpoints, branches, databases, and users that belong to the project.


### Example Usage

```python
import neon_api
from neon_api.models import operations

s = neon_api.NeonAPI(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.DeleteProjectRequest(
    project_id='cupiditate',
)

res = s.project.delete_project(req)

if res.project_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.DeleteProjectRequest](../../models/operations/deleteprojectrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |


### Response

**[operations.DeleteProjectResponse](../../models/operations/deleteprojectresponse.md)**


## get_project

Retrieves information about the specified project.
A project is the top-level object in the Neon object hierarchy.
You can obtain a `project_id` by listing the projects for your Neon account.


### Example Usage

```python
import neon_api
from neon_api.models import operations

s = neon_api.NeonAPI(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.GetProjectRequest(
    project_id='quos',
)

res = s.project.get_project(req)

if res.project_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `request`                                                                    | [operations.GetProjectRequest](../../models/operations/getprojectrequest.md) | :heavy_check_mark:                                                           | The request object to use for the request.                                   |


### Response

**[operations.GetProjectResponse](../../models/operations/getprojectresponse.md)**


## list_projects

Retrieves a list of projects for the Neon account.
A project is the top-level object in the Neon object hierarchy.
For more information, see [Manage projects](https://neon.tech/docs/manage/projects/).


### Example Usage

```python
import neon_api
from neon_api.models import operations

s = neon_api.NeonAPI(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.ListProjectsRequest(
    cursor='perferendis',
    limit=164940,
)

res = s.project.list_projects(req)

if res.list_projects_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.ListProjectsRequest](../../models/operations/listprojectsrequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |


### Response

**[operations.ListProjectsResponse](../../models/operations/listprojectsresponse.md)**


## update_project

Updates the specified project.
You can obtain a `project_id` by listing the projects for your Neon account.
Neon permits updating the project name only.


### Example Usage

```python
import neon_api
from neon_api.models import operations, shared

s = neon_api.NeonAPI(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.UpdateProjectRequest(
    project_update_request=shared.ProjectUpdateRequest(
        project=shared.ProjectUpdateRequestProject(
            default_endpoint_settings={
                "ipsam": 'alias',
                "fugit": 'dolorum',
                "excepturi": 'tempora',
                "facilis": 'tempore',
            },
            name='Lucia Kemmer',
            settings=shared.ProjectSettingsData(
                quota=shared.ProjectQuota(
                    active_time_seconds=576157,
                    compute_time_seconds=396098,
                    data_transfer_bytes=592042,
                    logical_size_bytes=896039,
                    written_data_bytes=572252,
                ),
            ),
        ),
    ),
    project_id='officia',
)

res = s.project.update_project(req)

if res.project_operations is not None:
    # handle response
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.UpdateProjectRequest](../../models/operations/updateprojectrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |


### Response

**[operations.UpdateProjectResponse](../../models/operations/updateprojectresponse.md)**

