"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import endpointoperations as shared_endpointoperations
from ..shared import generalerror as shared_generalerror
from typing import Optional



@dataclasses.dataclass
class SuspendProjectEndpointRequest:
    endpoint_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'endpoint_id', 'style': 'simple', 'explode': False }})
    r"""The endpoint ID"""
    project_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project_id', 'style': 'simple', 'explode': False }})
    r"""The Neon project ID"""
    




@dataclasses.dataclass
class SuspendProjectEndpointResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    endpoint_operations: Optional[shared_endpointoperations.EndpointOperations] = dataclasses.field(default=None)
    r"""Suspended the specified endpoint"""
    general_error: Optional[shared_generalerror.GeneralError] = dataclasses.field(default=None)
    r"""General Error"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    

