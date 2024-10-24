"""
File: cenhomes_models.py
Desc: Pydantic models for initial extracted output from cenhomes.vn
"""

from typing import List, Optional

from pydantic import BaseModel


class CenhomesShortInfo(BaseModel):
    listing_price: str
    unit_price: List[str]


class CenhomesImagesSection(BaseModel):
    images: List[str]


class CenhomesFeature(BaseModel):
    title: str
    value: Optional[str]


class CenhomesPropertyInfo(BaseModel):
    address: str
    title: str
    short_info: CenhomesShortInfo
    description: List[str]
    phone: str
    images_section: CenhomesImagesSection
    features: List[CenhomesFeature]
