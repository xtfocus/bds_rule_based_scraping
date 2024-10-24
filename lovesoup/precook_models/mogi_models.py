from typing import List, Optional

from pydantic import BaseModel


class MogiFeature(BaseModel):
    title: str
    value: str


class MogiPropertyInfo(BaseModel):
    title: str
    address: str
    listing_price: str
    features: List[MogiFeature]
    description: Optional[str] = None
    phone: Optional[str] = None
    images: List[str]
