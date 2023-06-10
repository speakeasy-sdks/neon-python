"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import generalerror as shared_generalerror
from ..shared import rolepasswordresponse as shared_rolepasswordresponse
from typing import Optional



@dataclasses.dataclass
class GetProjectBranchRolePasswordRequest:
    branch_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'branch_id', 'style': 'simple', 'explode': False }})
    r"""The branch ID"""
    project_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project_id', 'style': 'simple', 'explode': False }})
    r"""The Neon project ID"""
    role_name: str = dataclasses.field(metadata={'path_param': { 'field_name': 'role_name', 'style': 'simple', 'explode': False }})
    r"""The role name"""
    




@dataclasses.dataclass
class GetProjectBranchRolePasswordResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    general_error: Optional[shared_generalerror.GeneralError] = dataclasses.field(default=None)
    r"""Role not found"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    role_password_response: Optional[shared_rolepasswordresponse.RolePasswordResponse] = dataclasses.field(default=None)
    r"""Successfully returned password for the specified role"""
    

