# CreateProject201ApplicationJSON

Created a project.
The project includes a connection URI with a database, password, and role.
At least one non-protected role is created with a password.
Wait until the operations are finished before attempting to connect to a project database.



## Fields

| Field                                                                      | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `branch`                                                                   | [shared.Branch](../../models/shared/branch.md)                             | :heavy_check_mark:                                                         | N/A                                                                        |
| `connection_uris`                                                          | list[[shared.ConnectionDetails](../../models/shared/connectiondetails.md)] | :heavy_check_mark:                                                         | N/A                                                                        |
| `databases`                                                                | list[[shared.Database](../../models/shared/database.md)]                   | :heavy_check_mark:                                                         | N/A                                                                        |
| `endpoints`                                                                | list[[shared.Endpoint](../../models/shared/endpoint.md)]                   | :heavy_check_mark:                                                         | N/A                                                                        |
| `operations`                                                               | list[[shared.Operation](../../models/shared/operation.md)]                 | :heavy_check_mark:                                                         | N/A                                                                        |
| `project`                                                                  | [shared.Project](../../models/shared/project.md)                           | :heavy_check_mark:                                                         | N/A                                                                        |
| `roles`                                                                    | list[[shared.Role](../../models/shared/role.md)]                           | :heavy_check_mark:                                                         | N/A                                                                        |