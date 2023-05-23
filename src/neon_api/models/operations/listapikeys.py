"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import apikeyslistresponseitem as shared_apikeyslistresponseitem
from ..shared import generalerror as shared_generalerror
from typing import Optional


@dataclasses.dataclass
class ListAPIKeysResponse:
    
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    api_keys_list_response_items: Optional[list[shared_apikeyslistresponseitem.APIKeysListResponseItem]] = dataclasses.field(default=None)
    r"""Returned the API keys for the Neon account"""
    general_error: Optional[shared_generalerror.GeneralError] = dataclasses.field(default=None)
    r"""General Error"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    