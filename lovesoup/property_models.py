"""
File: property_info.py
Desc: Pydantic models for unified representation of properties on different sites
"""

from typing import List, Optional

from pydantic import BaseModel


class Address(BaseModel):
    full_address: Optional[str] = None
    house_no: Optional[str] = None
    alley: Optional[str] = None
    street: Optional[str] = None
    ward: Optional[str] = None
    district: Optional[str] = None
    province: Optional[str] = None


class Location(BaseModel):
    position: Optional[str] = None
    alley_position: Optional[str] = None
    distance_to_main_road: Optional[str] = None
    secondary_alley: Optional[str] = None


class Measurement(BaseModel):
    area: Optional[str] = None
    frontage: Optional[str] = None


class PropertyNormalized(BaseModel):
    address: Optional[Address] = None
    location: Optional[Location] = None
    area: Optional[Measurement] = None
    land_type: Optional[str] = None
    listing_price: Optional[str] = None
    unit_price: Optional[str] = None
    images: Optional[List[str]] = None
