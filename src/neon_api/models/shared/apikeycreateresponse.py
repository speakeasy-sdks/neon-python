"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from neon_api import utils


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class APIKeyCreateResponse:
    r"""Created an API key"""
    id: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    r"""The API key ID"""
    key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('key') }})
    r"""The generated 64-bit token required to access the Neon API"""
    

