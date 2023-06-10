# api_key

## Overview

These methods allow you to create and manage API keys for your Neon account. For related information, see [Manage API keys](https://neon.tech/docs/manage/api-keys).

### Available Operations

* [create_api_key](#create_api_key) - Create an API key
* [list_api_keys](#list_api_keys) - Get a list of API keys
* [revoke_api_key](#revoke_api_key) - Revoke an API key

## create_api_key

Creates an API key.
The `key_name` is a user-specified name for the key.
This method returns an `id` and `key`. The `key` is a randomly generated, 64-bit token required to access the Neon API.
API keys can also be managed in the Neon Console.
See [Manage API keys](https://neon.tech/docs/manage/api-keys/).


### Example Usage

```python
import neon_api
from neon_api.models import shared

s = neon_api.NeonAPI(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = shared.APIKeyCreateRequest(
    key_name='provident',
)

res = s.api_key.create_api_key(req)

if res.api_key_create_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `request`                                                                | [shared.APIKeyCreateRequest](../../models/shared/apikeycreaterequest.md) | :heavy_check_mark:                                                       | The request object to use for the request.                               |


### Response

**[operations.CreateAPIKeyResponse](../../models/operations/createapikeyresponse.md)**


## list_api_keys

Retrieves the API keys for your Neon account.
The response does not include API key tokens. A token is only provided when creating an API key.
API keys can also be managed in the Neon Console.
For more information, see [Manage API keys](https://neon.tech/docs/manage/api-keys/).


### Example Usage

```python
import neon_api


s = neon_api.NeonAPI(
    security=shared.Security(
        bearer_auth="",
    ),
)


res = s.api_key.list_api_keys()

if res.api_keys_list_response_items is not None:
    # handle response
```


### Response

**[operations.ListAPIKeysResponse](../../models/operations/listapikeysresponse.md)**


## revoke_api_key

Revokes the specified API key.
An API key that is no longer needed can be revoked.
This action cannot be reversed.
You can obtain `key_id` values by listing the API keys for your Neon account.
API keys can also be managed in the Neon Console.
See [Manage API keys](https://neon.tech/docs/manage/api-keys/).


### Example Usage

```python
import neon_api
from neon_api.models import operations

s = neon_api.NeonAPI(
    security=shared.Security(
        bearer_auth="",
    ),
)

req = operations.RevokeAPIKeyRequest(
    key_id=715190,
)

res = s.api_key.revoke_api_key(req)

if res.api_key_revoke_response is not None:
    # handle response
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.RevokeAPIKeyRequest](../../models/operations/revokeapikeyrequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |


### Response

**[operations.RevokeAPIKeyResponse](../../models/operations/revokeapikeyresponse.md)**

