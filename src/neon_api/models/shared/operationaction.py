"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum

class OperationAction(str, Enum):
    r"""The action performed by the operation"""
    CREATE_COMPUTE = 'create_compute'
    CREATE_TIMELINE = 'create_timeline'
    START_COMPUTE = 'start_compute'
    SUSPEND_COMPUTE = 'suspend_compute'
    APPLY_CONFIG = 'apply_config'
    CHECK_AVAILABILITY = 'check_availability'
    DELETE_TIMELINE = 'delete_timeline'
    CREATE_BRANCH = 'create_branch'
    TENANT_IGNORE = 'tenant_ignore'
    TENANT_ATTACH = 'tenant_attach'
    TENANT_DETACH = 'tenant_detach'
    TENANT_REATTACH = 'tenant_reattach'
    REPLACE_SAFEKEEPER = 'replace_safekeeper'
    DISABLE_MAINTENANCE = 'disable_maintenance'
