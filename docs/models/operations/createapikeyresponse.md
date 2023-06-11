# CreateAPIKeyResponse


## Fields

| Field                                                                                 | Type                                                                                  | Required                                                                              | Description                                                                           |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `api_key_create_response`                                                             | [Optional[shared.APIKeyCreateResponse]](../../models/shared/apikeycreateresponse.md)  | :heavy_minus_sign:                                                                    | Created an API key                                                                    |
| `content_type`                                                                        | *str*                                                                                 | :heavy_check_mark:                                                                    | N/A                                                                                   |
| `general_error`                                                                       | [Optional[shared.GeneralError]](../../models/shared/generalerror.md)                  | :heavy_minus_sign:                                                                    | General Error                                                                         |
| `status_code`                                                                         | *int*                                                                                 | :heavy_check_mark:                                                                    | N/A                                                                                   |
| `raw_response`                                                                        | [requests.Response](https://requests.readthedocs.io/en/latest/api/#requests.Response) | :heavy_minus_sign:                                                                    | N/A                                                                                   |