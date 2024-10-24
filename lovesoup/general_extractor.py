"""
File: extract.py
Desc: General extractor function based on template
"""

import importlib.resources as pkg_resources
import re
import unicodedata
from abc import ABC, abstractmethod
from typing import Annotated, Dict, Optional

from loguru import logger
from pydantic import BaseModel, HttpUrl, validator
from pydantic.functional_validators import AfterValidator
from selectorlib import Extractor

from lovesoup import precook_templates
from lovesoup.property_models import PropertyNormalized


def read_yaml_file(file_name: str) -> str:
    """
    Open the file within the templates folder

    """
    try:
        with pkg_resources.open_text(precook_templates, file_name) as yaml_file:
            content = yaml_file.read()
            return content
    except Exception as e:
        logger.error(f"Error loading template file {file_name}\n Error: {e}")
        raise


class DataExtractor(ABC):
    def __init__(self, template_name: str):
        self.template = template_name
        self.extractor = Extractor.from_yaml_string(
            read_yaml_file(f"{template_name}.yaml")
        )

    def exec_precook(self, source_path: str) -> Dict:
        try:
            # Read the HTML content from the provided source path
            with open(source_path, "r", encoding="utf-8") as file:
                html_content = file.read()

        except Exception as e:
            logger.error(f"Error reading file: {e}")
            raise
        # Extract data using the template
        extracted_data = self.extractor.extract(html_content)

        return extracted_data

    @abstractmethod
    def post_process(self, primary_result: Dict) -> PropertyNormalized:
        raise NotImplementedError

    def run(self, source_path: str):
        primary_result = self.exec_precook(source_path)
        return self.post_process(primary_result)

    def run_html(self, html_content: str):
        primary_result = self.extractor.extract(html_content)
        return self.post_process(primary_result)


def extract_image_url(text: str) -> str:
    # Pattern to match src or data-src
    match = re.search(r'(?:src|data-src)="(https?://[^"]+)"', text)
    if match:
        return match.group(1)
    return ""


# Create a type alias for VinaStr with constraints using Annotated
VinaStr = Annotated[
    str,
    AfterValidator((lambda x: unicodedata.normalize("NFC", x).replace("\xa0", " "))),
]
