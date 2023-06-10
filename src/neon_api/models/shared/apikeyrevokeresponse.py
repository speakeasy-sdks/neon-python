"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from marshmallow import fields
from neon_api import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class APIKeyRevokeResponse:
    r"""Revoked the specified API key"""
    id: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    r"""The API key ID"""
    last_used_from_addr: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('last_used_from_addr') }})
    r"""The IP address from which the API key was last used"""
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    r"""The user-specified API key name"""
    revoked: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('revoked') }})
    r"""A `true` or `false` value indicating whether the API key is revoked"""
    last_used_at: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('last_used_at'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    r"""A timestamp indicating when the API was last used"""
    

