from typing import Dict, List, Optional

from pydantic import BaseModel


class MuabannetPropertyInfo(BaseModel):
    address: str
    phone: List[str]
    images: List[str]
    short_info: List[Dict[str, List]]
    listing_price: str
    description: str
    features: List[str]
