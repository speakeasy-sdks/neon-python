"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from .sdkconfiguration import SDKConfiguration
from neon_api import utils
from neon_api.models import operations, shared
from typing import Optional

class APIKey:
    r"""These methods allow you to create and manage API keys for your Neon account. For related information, see [Manage API keys](https://neon.tech/docs/manage/api-keys)."""
    sdk_configuration: SDKConfiguration

    def __init__(self, sdk_config: SDKConfiguration) -> None:
        self.sdk_configuration = sdk_config
        
    
    def create_api_key(self, request: shared.APIKeyCreateRequest) -> operations.CreateAPIKeyResponse:
        r"""Create an API key
        Creates an API key.
        The `key_name` is a user-specified name for the key.
        This method returns an `id` and `key`. The `key` is a randomly generated, 64-bit token required to access the Neon API.
        API keys can also be managed in the Neon Console.
        See [Manage API keys](https://neon.tech/docs/manage/api-keys/).
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = base_url + '/api_keys'
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "request", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        headers['Accept'] = 'application/json;q=1, application/json;q=0'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version} {self.sdk_configuration.openapi_doc_version}'
        
        client = self.sdk_configuration.security_client
        
        http_res = client.request('POST', url, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.CreateAPIKeyResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.APIKeyCreateResponse])
                res.api_key_create_response = out
        else:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.GeneralError])
                res.general_error = out

        return res

    
    def list_api_keys(self) -> operations.ListAPIKeysResponse:
        r"""Get a list of API keys
        Retrieves the API keys for your Neon account.
        The response does not include API key tokens. A token is only provided when creating an API key.
        API keys can also be managed in the Neon Console.
        For more information, see [Manage API keys](https://neon.tech/docs/manage/api-keys/).
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = base_url + '/api_keys'
        headers = {}
        headers['Accept'] = 'application/json;q=1, application/json;q=0'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version} {self.sdk_configuration.openapi_doc_version}'
        
        client = self.sdk_configuration.security_client
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.ListAPIKeysResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[list[shared.APIKeysListResponseItem]])
                res.api_keys_list_response_items = out
        else:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.GeneralError])
                res.general_error = out

        return res

    
    def revoke_api_key(self, request: operations.RevokeAPIKeyRequest) -> operations.RevokeAPIKeyResponse:
        r"""Revoke an API key
        Revokes the specified API key.
        An API key that is no longer needed can be revoked.
        This action cannot be reversed.
        You can obtain `key_id` values by listing the API keys for your Neon account.
        API keys can also be managed in the Neon Console.
        See [Manage API keys](https://neon.tech/docs/manage/api-keys/).
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.RevokeAPIKeyRequest, base_url, '/api_keys/{key_id}', request)
        headers = {}
        headers['Accept'] = 'application/json;q=1, application/json;q=0'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version} {self.sdk_configuration.openapi_doc_version}'
        
        client = self.sdk_configuration.security_client
        
        http_res = client.request('DELETE', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.RevokeAPIKeyResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.APIKeyRevokeResponse])
                res.api_key_revoke_response = out
        else:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.GeneralError])
                res.general_error = out

        return res

    