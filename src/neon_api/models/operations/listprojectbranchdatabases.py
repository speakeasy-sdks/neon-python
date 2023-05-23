"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import databasesresponse as shared_databasesresponse
from ..shared import generalerror as shared_generalerror
from typing import Optional


@dataclasses.dataclass
class ListProjectBranchDatabasesRequest:
    
    branch_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'branch_id', 'style': 'simple', 'explode': False }})
    r"""The branch ID"""
    project_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project_id', 'style': 'simple', 'explode': False }})
    r"""The Neon project ID"""
    

@dataclasses.dataclass
class ListProjectBranchDatabasesResponse:
    
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    databases_response: Optional[shared_databasesresponse.DatabasesResponse] = dataclasses.field(default=None)
    r"""Returned a list of databases of the specified branch"""
    general_error: Optional[shared_generalerror.GeneralError] = dataclasses.field(default=None)
    r"""General Error"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    