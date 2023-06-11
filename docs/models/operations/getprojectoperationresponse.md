# GetProjectOperationResponse


## Fields

| Field                                                                                 | Type                                                                                  | Required                                                                              | Description                                                                           |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `content_type`                                                                        | *str*                                                                                 | :heavy_check_mark:                                                                    | N/A                                                                                   |
| `general_error`                                                                       | [Optional[shared.GeneralError]](../../models/shared/generalerror.md)                  | :heavy_minus_sign:                                                                    | General Error                                                                         |
| `operation_response`                                                                  | [Optional[shared.OperationResponse]](../../models/shared/operationresponse.md)        | :heavy_minus_sign:                                                                    | Returned details for the specified operation                                          |
| `status_code`                                                                         | *int*                                                                                 | :heavy_check_mark:                                                                    | N/A                                                                                   |
| `raw_response`                                                                        | [requests.Response](https://requests.readthedocs.io/en/latest/api/#requests.Response) | :heavy_minus_sign:                                                                    | N/A                                                                                   |