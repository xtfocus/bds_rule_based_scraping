"""
File: batdongsan_models.py
Desc: Pydantic models for initial extracted output from batdongsan.com.vn
"""

from typing import List, Optional

from pydantic import BaseModel


class BatDongSanShortInfoItem(BaseModel):
    title: str
    value: str
    sub: Optional[str] = None


class BatDongSanShortInfo(BaseModel):
    item: List[BatDongSanShortInfoItem]


class BatDongSanAdInfoItem(BaseModel):
    title: str
    value: str


class BatDongSanAdInfo(BaseModel):
    item: List[BatDongSanAdInfoItem]


class BatDongSanFeature(BaseModel):
    title: str
    value: str


class BatDongSanPropertyInfo(BaseModel):
    post_title: str
    address: str
    short_info: BatDongSanShortInfo
    ad_info: BatDongSanAdInfo
    description: str
    features: List[BatDongSanFeature]
    phone: str
    images: List[str]
