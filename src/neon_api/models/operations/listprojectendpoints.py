"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import endpointsresponse as shared_endpointsresponse
from ..shared import generalerror as shared_generalerror
from typing import Optional


@dataclasses.dataclass
class ListProjectEndpointsRequest:
    
    project_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project_id', 'style': 'simple', 'explode': False }})
    r"""The Neon project ID"""
    

@dataclasses.dataclass
class ListProjectEndpointsResponse:
    
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    endpoints_response: Optional[shared_endpointsresponse.EndpointsResponse] = dataclasses.field(default=None)
    r"""Returned a list of endpoints for the specified project"""
    general_error: Optional[shared_generalerror.GeneralError] = dataclasses.field(default=None)
    r"""General Error"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    