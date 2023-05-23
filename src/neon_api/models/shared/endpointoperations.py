"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import endpoint as shared_endpoint
from ..shared import operation as shared_operation
from dataclasses_json import Undefined, dataclass_json
from neon_api import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class EndpointOperations:
    r"""Created an endpoint"""
    
    endpoint: shared_endpoint.Endpoint = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('endpoint') }})
    operations: list[shared_operation.Operation] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('operations') }})
    