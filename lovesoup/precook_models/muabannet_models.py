from typing import Dict, List, Optional

from pydantic import BaseModel


class MuabannetPropertyInfo(BaseModel):
    address: Optional[str]
    phone: Optional[List[str]]
    images: Optional[List[str]]
    short_info: Optional[List[Dict[str, List]]]
    listing_price: Optional[str]
    description: Optional[str]
    features: Optional[List[str]]
