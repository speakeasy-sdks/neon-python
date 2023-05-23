"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum

class EndpointState(str, Enum):
    r"""The state of the compute endpoint"""
    INIT = 'init'
    ACTIVE = 'active'
    IDLE = 'idle'
