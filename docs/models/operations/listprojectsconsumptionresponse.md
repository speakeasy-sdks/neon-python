# ListProjectsConsumptionResponse


## Fields

| Field                                                                                                                       | Type                                                                                                                        | Required                                                                                                                    | Description                                                                                                                 |
| --------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| `content_type`                                                                                                              | *str*                                                                                                                       | :heavy_check_mark:                                                                                                          | N/A                                                                                                                         |
| `general_error`                                                                                                             | [Optional[shared.GeneralError]](../../models/shared/generalerror.md)                                                        | :heavy_minus_sign:                                                                                                          | General Error                                                                                                               |
| `status_code`                                                                                                               | *int*                                                                                                                       | :heavy_check_mark:                                                                                                          | N/A                                                                                                                         |
| `raw_response`                                                                                                              | [requests.Response](https://requests.readthedocs.io/en/latest/api/#requests.Response)                                       | :heavy_minus_sign:                                                                                                          | N/A                                                                                                                         |
| `list_projects_consumption_200_application_json_object`                                                                     | [Optional[ListProjectsConsumption200ApplicationJSON]](../../models/operations/listprojectsconsumption200applicationjson.md) | :heavy_minus_sign:                                                                                                          | Returned a list of per-project consumption for the Neon account                                                             |