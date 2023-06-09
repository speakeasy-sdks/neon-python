"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from neon_api import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DatabaseCreateRequestDatabase:
    
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    r"""The name of the datbase"""
    owner_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('owner_name') }})
    r"""The name of the role that owns the database"""
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DatabaseCreateRequest:
    
    database: DatabaseCreateRequestDatabase = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('database') }})
    