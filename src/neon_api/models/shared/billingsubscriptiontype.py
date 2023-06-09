"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum

class BillingSubscriptionType(str, Enum):
    r"""Type of subscription to Neon Cloud.
    Notice that for users without billing account this will be \"UNKNOWN\" 
    """
    UNKNOWN = 'UNKNOWN'
    FREE = 'free'
    PRO = 'pro'
    PLATFORM_PARTNERSHIP = 'platform_partnership'
    ENTERPRISE = 'enterprise'
