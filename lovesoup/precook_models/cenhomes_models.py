"""
File: cenhomes_models.py
Desc: Pydantic models for initial extracted output from cenhomes.vn
"""

from typing import List, Optional

from pydantic import BaseModel


class CenhomesShortInfo(BaseModel):
    listing_price: Optional[str] = ""
    unit_price: Optional[List[str]] = []


class CenhomesImagesSection(BaseModel):
    images: Optional[List[str]] = []


class CenhomesFeature(BaseModel):
    title: Optional[str]
    value: Optional[str]


class CenhomesPropertyInfo(BaseModel):
    address: Optional[str]
    title: Optional[str]
    short_info: Optional[CenhomesShortInfo] = CenhomesShortInfo()
    description: Optional[List[str]] = []
    phone: Optional[str]
    images_section: Optional[CenhomesImagesSection]
    features: Optional[List[CenhomesFeature]] = []
    geolocation: Optional[List[CenhomesFeature]] = []
