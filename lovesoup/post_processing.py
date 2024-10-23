"""
File: post_processing.py
Desc: Specific post-processor depends on the site/template
"""

import json

from .batdongsan_models import BatDongSanPropertyInfo
from .bds123vn_models import BDS123VnPropertyInfo
from .cenhomes_models import CenhomesPropertyInfo
from .general_extractor import DataExtractor, ImageURL
from .mogi_models import MogiPropertyInfo
from .muabannet_models import MuabannetPropertyInfo
from .nhatot_models import NhatotPropertyInfo
from .property_models import Address, Location, Measurement, PropertyNormalized


class Mogi(DataExtractor):
    def __init__(self, template_name="mogi"):
        super().__init__(template_name)

    def post_process(self, res: MogiPropertyInfo):
        res = MogiPropertyInfo.model_validate(res)
        address = Address(full_address=res.address)

        location = Location(
            position="", alley_position="", distance_to_main_road="", secondary_alley=""
        )

        # Extract area and frontage from features
        area = Measurement(
            area=next(
                (f.value for f in res.features if f.title == "Diện tích đất"), ""
            ),
            frontage="",  # Assuming frontage is not available in this dataset
        )
        listing_price = res.listing_price
        unit_price = None
        images = [str(ImageURL(raw_string=i).url) for i in res.images]
        # Create and return PropertyNormalized object
        return PropertyNormalized(
            address=address,
            location=location,
            area=area,
            land_type="",  # Assuming land_type is not available in this dataset
            listing_price=listing_price,
            unit_price=unit_price,
            images=images,
        )


class BatDongSan(DataExtractor):
    def __init__(self, template_name="batdongsancomvn"):
        super().__init__(template_name)

    def post_process(self, res: BatDongSanPropertyInfo):
        res = BatDongSanPropertyInfo.model_validate(res)

        address = Address(full_address=res.address)

        location = Location(
            position="", alley_position="", distance_to_main_road="", secondary_alley=""
        )

        # Extract area and frontage from features
        area = Measurement(
            area=next((f.value for f in res.features if f.title == "Diện tích"), ""),
            frontage="",  # Assuming frontage is not available in this dataset
        )

        # Extract other necessary fields
        listing_price = next(
            (f.value for f in res.features if f.title == "Mức giá"), ""
        )
        unit_price = next(
            (f.sub for f in res.short_info.item if f.title == "Mức giá"), ""
        )

        # Create and return PropertyNormalized object
        return PropertyNormalized(
            address=address,
            location=location,
            area=area,
            land_type="",  # Assuming land_type is not available in this dataset
            listing_price=listing_price,
            unit_price=unit_price,
            images=res.images,
        )


class Cenhomes(DataExtractor):
    def __init__(self, template_name="cenhomes"):
        super().__init__(template_name)

    def post_process(self, res: CenhomesPropertyInfo):
        res = CenhomesPropertyInfo.model_validate(res)

        address = Address(full_address=res.address)

        location = Location(
            position="", alley_position="", distance_to_main_road="", secondary_alley=""
        )

        # Extract area and frontage from features
        area = Measurement(
            area=next((f.value for f in res.features if f.title == "Diện tích:"), ""),
            frontage="",  # Assuming frontage is not available in this dataset
        )

        # Extract other necessary fields
        listing_price = res.short_info.listing_price
        unit_price = res.short_info.unit_price[0]

        # Create and return PropertyNormalized object
        return PropertyNormalized(
            address=address,
            location=location,
            area=area,
            land_type="",  # Assuming land_type is not available in this dataset
            listing_price=listing_price,
            unit_price=unit_price,
            images=res.images_section.images,
        )


class BDS123Vn(DataExtractor):
    def __init__(self, template_name="bds123vn"):
        super().__init__(template_name)

    def post_process(self, res: BDS123VnPropertyInfo):
        res = BDS123VnPropertyInfo.model_validate(res)

        address = Address(full_address=res.address)

        location = Location(
            position="", alley_position="", distance_to_main_road="", secondary_alley=""
        )

        # Extract area and frontage from features
        area = Measurement(
            area=next(
                (f.value for f in res.short_info if f.title == "item post-acreage"), ""
            ),
            frontage="",  # Assuming frontage is not available in this dataset
        )

        listing_price = next(
            (f.value for f in res.short_info if f.title == "item post-price"), ""
        )
        unit_price = None

        # Create and return PropertyNormalized object
        return PropertyNormalized(
            address=address,
            location=location,
            area=area,
            land_type="",  # Assuming land_type is not available in this dataset
            listing_price=listing_price,
            unit_price=unit_price,
            images=res.images_section.images,
        )


class Muabannet(DataExtractor):
    def __init__(self, template_name="muabannet"):
        super().__init__(template_name)

    def post_process(self, res: MuabannetPropertyInfo):
        res = MuabannetPropertyInfo.model_validate(res)

        address = Address(full_address=res.address)

        location = Location(
            position="", alley_position="", distance_to_main_road="", secondary_alley=""
        )

        # Extract area and frontage from features
        area = Measurement(
            area=next(
                (
                    f["item"][1]
                    for f in res.short_info
                    if f["item"][0] == "Diện tích sử dụng :"
                ),
                "",
            ),
            frontage="",
        )

        listing_price = res.listing_price
        unit_price = None
        images = [str(ImageURL(raw_string=i).url) for i in res.images]

        # Create and return PropertyNormalized object
        return PropertyNormalized(
            address=address,
            location=location,
            area=area,
            land_type="",
            listing_price=listing_price,
            unit_price=unit_price,
            images=images,
        )


class Nhatot(DataExtractor):
    def __init__(self, template_name="nhatot"):
        super().__init__(template_name)

    def post_process(self, res) -> PropertyNormalized:
        location = Location(
            position="", alley_position="", distance_to_main_road="", secondary_alley=""
        )

        listing_price = res["pricing"].get("listing_price")
        unit_price = res["pricing"].get("unit_price")

        data = json.loads(res["ad_details"])["props"]["pageProps"]["initialState"][
            "adView"
        ]["adInfo"]["ad"]

        images = data["images"]

        area = Measurement(
            area=str(data.get("size")) + data.get("size_unit_string"),
            frontage="",
        )

        address = Address(
            full_address="",  # Can be inferred from other. Create another constructor method here would be nice
            ward=data.get("ward_name"),
            district=data.get("area_name"),
            street=data.get("street_name"),
        )
        # Create and return PropertyNormalized object
        return PropertyNormalized(
            address=address,
            location=location,
            area=area,
            land_type=data.get("category_name"),
            listing_price=listing_price,
            unit_price=unit_price,
            images=images,
        )
