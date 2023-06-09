"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import endpointtype as shared_endpointtype
from ..shared import provisioner as shared_provisioner
from dataclasses_json import Undefined, dataclass_json
from neon_api import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class BranchCreateRequestEndpointOptions:
    
    type: shared_endpointtype.EndpointType = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type') }})
    r"""The compute endpoint type. Either `read_write` or `read_only`.
    The `read_only` compute endpoint type is not yet supported.
    """
    autoscaling_limit_max_cu: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('autoscaling_limit_max_cu'), 'exclude': lambda f: f is None }})
    autoscaling_limit_min_cu: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('autoscaling_limit_min_cu'), 'exclude': lambda f: f is None }})
    provisioner: Optional[shared_provisioner.Provisioner] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('provisioner'), 'exclude': lambda f: f is None }})
    r"""The Neon compute provisioner."""
    suspend_timeout_seconds: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('suspend_timeout_seconds'), 'exclude': lambda f: f is None }})
    r"""Duration of inactivity in seconds after which endpoint will be
    automatically suspended. Value `0` means use global default,
    `-1` means never suspend. Maximum value is 1 week in seconds.
    """
    