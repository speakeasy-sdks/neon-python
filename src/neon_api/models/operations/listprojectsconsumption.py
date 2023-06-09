"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import generalerror as shared_generalerror
from ..shared import pagination as shared_pagination
from ..shared import projectconsumption as shared_projectconsumption
from dataclasses_json import Undefined, dataclass_json
from neon_api import utils
from typing import Optional


@dataclasses.dataclass
class ListProjectsConsumptionRequest:
    
    cursor: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'cursor', 'style': 'form', 'explode': True }})
    r"""Specify the cursor value from the previous response to get the next batch of projects."""
    limit: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'limit', 'style': 'form', 'explode': True }})
    r"""Specify a value from 1 to 1000 to limit number of projects in the response."""
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ListProjectsConsumption200ApplicationJSON:
    r"""Returned a list of per-project consumption for the Neon account"""
    
    projects: list[shared_projectconsumption.ProjectConsumption] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('projects') }})
    pagination: Optional[shared_pagination.Pagination] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('pagination'), 'exclude': lambda f: f is None }})
    r"""Cursor based pagination is used. The user must pass the cursor as is to the backend.
    For more information about cursor based pagination, see
    https://learn.microsoft.com/en-us/ef/core/querying/pagination#keyset-pagination
    """
    

@dataclasses.dataclass
class ListProjectsConsumptionResponse:
    
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    general_error: Optional[shared_generalerror.GeneralError] = dataclasses.field(default=None)
    r"""General Error"""
    list_projects_consumption_200_application_json_object: Optional[ListProjectsConsumption200ApplicationJSON] = dataclasses.field(default=None)
    r"""Returned a list of per-project consumption for the Neon account"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    