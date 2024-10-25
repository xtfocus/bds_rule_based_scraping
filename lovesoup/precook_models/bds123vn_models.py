from typing import List, Optional

from pydantic import BaseModel

from lovesoup.general_extractor import VinaStr


class BDS123VnShortInfo(BaseModel):
    title: Optional[str] = None
    value: Optional[str] = None


class BDS123VnFeatureItem(BaseModel):
    item: Optional[List[VinaStr]] = []


class BDS123VnPropertyInfo(BaseModel):
    address: Optional[str] = None
    phone_number: Optional[str] = None
    images: Optional[List[str]] = None
    description: Optional[List[str]] = []
    title: Optional[str] = None
    short_info: Optional[List[BDS123VnShortInfo]] = []
    features: Optional[List[BDS123VnFeatureItem]] = []
