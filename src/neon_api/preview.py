"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from .sdkconfiguration import SDKConfiguration
from neon_api import utils
from neon_api.models import operations, shared
from typing import Optional

class Preview:
    r"""New API methods that are in Beta / Preview state and could be subjected to significant changes in the future."""
    sdk_configuration: SDKConfiguration

    def __init__(self, sdk_config: SDKConfiguration) -> None:
        self.sdk_configuration = sdk_config
        
    
    def list_projects_consumption(self, request: operations.ListProjectsConsumptionRequest) -> operations.ListProjectsConsumptionResponse:
        r"""Get a list of projects consumption
        Note, this is a preview API and could be subjected to significant changes in the future.
        Retrieves a list of per-project consumption for the current billing period.
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = base_url + '/consumption/projects'
        headers = {}
        query_params = utils.get_query_params(operations.ListProjectsConsumptionRequest, request)
        headers['Accept'] = 'application/json;q=1, application/json;q=0'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version} {self.sdk_configuration.openapi_doc_version}'
        
        client = self.sdk_configuration.security_client
        
        http_res = client.request('GET', url, params=query_params, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.ListProjectsConsumptionResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.ListProjectsConsumption200ApplicationJSON])
                res.list_projects_consumption_200_application_json_object = out
        else:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.GeneralError])
                res.general_error = out

        return res

    