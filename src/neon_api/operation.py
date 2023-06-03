"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from .sdkconfiguration import SDKConfiguration
from neon_api import utils
from neon_api.models import operations, shared
from typing import Optional

class Operation:
    r"""These methods allow you to view operation details for your Neon project. For related information, see [Operations](https://neon.tech/docs/manage/operations)."""
    sdk_configuration: SDKConfiguration

    def __init__(self, sdk_config: SDKConfiguration) -> None:
        self.sdk_configuration = sdk_config
        
    
    def get_project_operation(self, request: operations.GetProjectOperationRequest) -> operations.GetProjectOperationResponse:
        r"""Get operation details
        Retrieves details for the specified operation.
        An operation is an action performed on a Neon project resource.
        You can obtain a `project_id` by listing the projects for your Neon account.
        You can obtain a `operation_id` by listing operations for the project.
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.GetProjectOperationRequest, base_url, '/projects/{project_id}/operations/{operation_id}', request)
        headers = {}
        headers['Accept'] = 'application/json;q=1, application/json;q=0'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version}'
        
        client = self.sdk_configuration.security_client
        
        http_res = client.request('GET', url, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetProjectOperationResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.OperationResponse])
                res.operation_response = out
        else:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.GeneralError])
                res.general_error = out

        return res

    
    def list_project_operations(self, request: operations.ListProjectOperationsRequest) -> operations.ListProjectOperationsResponse:
        r"""Get a list of operations
        Retrieves a list of operations for the specified Neon project.
        You can obtain a `project_id` by listing the projects for your Neon account.
        The number of operations returned can be large.
        To paginate the response, issue an initial request with a `limit` value.
        Then, add the `cursor` value that was returned in the response to the next request.
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.ListProjectOperationsRequest, base_url, '/projects/{project_id}/operations', request)
        headers = {}
        query_params = utils.get_query_params(operations.ListProjectOperationsRequest, request)
        headers['Accept'] = 'application/json;q=1, application/json;q=0'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version}'
        
        client = self.sdk_configuration.security_client
        
        http_res = client.request('GET', url, params=query_params, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.ListProjectOperationsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.ListProjectOperations200ApplicationJSON])
                res.list_project_operations_200_application_json_object = out
        else:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.GeneralError])
                res.general_error = out

        return res

    