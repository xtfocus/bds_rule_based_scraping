"""
File: nhatot_models.py
Desc: Pydantic models for initial extracted output from nhatot.com
"""

from pydantic import BaseModel


class NhatotPricing(BaseModel):
    listing_price: str
    unit_price: str


class NhatotPropertyInfo(BaseModel):
    title: str
    pricing: NhatotPricing
    ad_details: str
