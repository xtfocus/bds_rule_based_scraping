"""
File: extract.py
Desc: General extractor function based on template
"""

import importlib.resources as pkg_resources
import re
from abc import ABC, abstractmethod
from typing import Dict, Optional

from loguru import logger
from pydantic import BaseModel, HttpUrl, validator
from selectorlib import Extractor

from . import templates  # Assuming templates is in the same package


# Open the file within the templates folder
def read_yaml_file(file_name):
    with pkg_resources.open_text(templates, file_name) as yaml_file:
        content = yaml_file.read()
        return content


class DataExtractor(ABC):
    def __init__(self, template_name: str):
        self.template = template_name
        file_name = f"{template_name}.yaml"
        self.extractor = Extractor.from_yaml_string(read_yaml_file(f"{file_name}"))

    def execute_template(self, source_path: str):
        try:
            # Read the HTML content from the provided source path
            with open(source_path, "r", encoding="utf-8") as file:
                html_content = file.read()
        except Exception as e:
            logger.error(f"Got error reading file: {e}")
            raise
        # Extract data using the template
        extracted_data = self.extractor.extract(html_content)

        return extracted_data

    @abstractmethod
    def post_process(self, primary_result: Dict) -> Dict:
        raise NotImplementedError

    def run(self, source_path: str) -> Dict:
        primary_result = self.execute_template(source_path)
        return self.post_process(primary_result)

    # def run_html(self, html_content: str):
    #     pri


class ImageURL(BaseModel):
    raw_string: str
    url: Optional[HttpUrl] = None

    @validator("url", always=True, pre=True)
    def extract_url(cls, v, values):
        # Pattern to match src or data-src
        match = re.search(r'(?:src|data-src)="(https?://[^"]+)"', values["raw_string"])
        if match:
            return match.group(1)
        raise ValueError("No valid URL found in the string")
