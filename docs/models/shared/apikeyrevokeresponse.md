# APIKeyRevokeResponse

Revoked the specified API key


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `id`                                                                 | *int*                                                                | :heavy_check_mark:                                                   | The API key ID                                                       |
| `last_used_at`                                                       | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_minus_sign:                                                   | A timestamp indicating when the API was last used                    |
| `last_used_from_addr`                                                | *str*                                                                | :heavy_check_mark:                                                   | The IP address from which the API key was last used                  |
| `name`                                                               | *str*                                                                | :heavy_check_mark:                                                   | The user-specified API key name                                      |
| `revoked`                                                            | *bool*                                                               | :heavy_check_mark:                                                   | A `true` or `false` value indicating whether the API key is revoked  |