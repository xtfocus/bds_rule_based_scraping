from typing import List, Optional

from pydantic import BaseModel


class BDS123VnImageSection(BaseModel):
    images: Optional[List[str]] = None


class BDS123VnShortInfo(BaseModel):
    title: str
    value: str


class BDS123VnFeatureItem(BaseModel):
    item: List[str]


class BDS123VnPropertyInfo(BaseModel):
    address: str
    phone_number: str
    images_section: BDS123VnImageSection
    description: List[str]
    title: str
    short_info: List[BDS123VnShortInfo]
    features: List[BDS123VnFeatureItem]
