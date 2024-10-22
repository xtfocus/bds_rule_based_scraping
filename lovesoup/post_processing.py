"""
File: post_processing.py
Desc: Specific post-processor depends on the site/template
"""

from .batdongsan_models import BatDongSanPropertyInfo
from .bds123vn_models import BDS123VnPropertyInfo
from .cenhomes_models import CenhomesPropertyInfo
from .general_extractor import DataExtractor
from .mogi_models import MogiPropertyInfo
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
