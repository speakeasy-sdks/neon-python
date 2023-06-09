"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import generalerror as shared_generalerror
from ..shared import rolecreaterequest as shared_rolecreaterequest
from ..shared import roleoperations as shared_roleoperations
from typing import Optional


@dataclasses.dataclass
class CreateProjectBranchRoleRequest:
    
    branch_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'branch_id', 'style': 'simple', 'explode': False }})
    r"""The branch ID"""
    project_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project_id', 'style': 'simple', 'explode': False }})
    r"""The Neon project ID"""
    role_create_request: shared_rolecreaterequest.RoleCreateRequest = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class CreateProjectBranchRoleResponse:
    
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    general_error: Optional[shared_generalerror.GeneralError] = dataclasses.field(default=None)
    r"""General Error"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    role_operations: Optional[shared_roleoperations.RoleOperations] = dataclasses.field(default=None)
    r"""Created a role in the specified branch"""
    