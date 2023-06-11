# ListProjectOperations200ApplicationJSON

Returned a list of operations



## Fields

| Field                                                                                                                                                                                                                         | Type                                                                                                                                                                                                                          | Required                                                                                                                                                                                                                      | Description                                                                                                                                                                                                                   |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `operations`                                                                                                                                                                                                                  | list[[shared.Operation](../../models/shared/operation.md)]                                                                                                                                                                    | :heavy_check_mark:                                                                                                                                                                                                            | N/A                                                                                                                                                                                                                           |
| `pagination`                                                                                                                                                                                                                  | [Optional[shared.Pagination]](../../models/shared/pagination.md)                                                                                                                                                              | :heavy_minus_sign:                                                                                                                                                                                                            | Cursor based pagination is used. The user must pass the cursor as is to the backend.<br/>For more information about cursor based pagination, see<br/>https://learn.microsoft.com/en-us/ef/core/querying/pagination#keyset-pagination<br/> |