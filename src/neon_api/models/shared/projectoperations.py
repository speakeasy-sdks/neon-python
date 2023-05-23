"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import operation as shared_operation
from ..shared import project as shared_project
from dataclasses_json import Undefined, dataclass_json
from neon_api import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ProjectOperations:
    r"""Updated the specified project"""
    
    operations: list[shared_operation.Operation] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('operations') }})
    project: shared_project.Project = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('project') }})
    