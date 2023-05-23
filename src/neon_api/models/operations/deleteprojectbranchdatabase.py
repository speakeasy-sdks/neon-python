"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import databaseoperations as shared_databaseoperations
from ..shared import generalerror as shared_generalerror
from typing import Optional


@dataclasses.dataclass
class DeleteProjectBranchDatabaseRequest:
    
    branch_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'branch_id', 'style': 'simple', 'explode': False }})
    r"""The branch ID"""
    database_name: str = dataclasses.field(metadata={'path_param': { 'field_name': 'database_name', 'style': 'simple', 'explode': False }})
    r"""The database name"""
    project_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project_id', 'style': 'simple', 'explode': False }})
    r"""The Neon project ID"""
    

@dataclasses.dataclass
class DeleteProjectBranchDatabaseResponse:
    
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    database_operations: Optional[shared_databaseoperations.DatabaseOperations] = dataclasses.field(default=None)
    r"""Deleted the specified database"""
    general_error: Optional[shared_generalerror.GeneralError] = dataclasses.field(default=None)
    r"""General Error"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    