"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import database as shared_database
from dataclasses_json import Undefined, dataclass_json
from neon_api import utils


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class DatabaseResponse:
    r"""Returned the database details"""
    database: shared_database.Database = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('database') }})
    

