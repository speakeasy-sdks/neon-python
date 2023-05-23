<!-- Start SDK Example Usage -->
```python
import neon_api
from neon_api.models import shared

s = neon_api.NeonAPI(
    security=shared.Security(
        bearer_auth="YOUR_BEARER_TOKEN_HERE",
    ),
)

req = shared.APIKeyCreateRequest(
    key_name='corrupti',
)

res = s.api_key.create_api_key(req)

if res.api_key_create_response is not None:
    # handle response
```
<!-- End SDK Example Usage -->