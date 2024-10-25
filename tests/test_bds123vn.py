"""
File: test_bds123vn.py
Desc: Simple test to make sure the dev doesn't break anything
"""

import json
import pathlib

from lovesoup.cooks import BDS123Vn

# Define the directory where the test data is located
TEST_DIR = pathlib.Path(__file__).parent / "test_data" / "bds123vn"


def test_bds123vn():
    # Initialize the extractor
    extractor = BDS123Vn()

    # Define the path to the sample HTML and JSON files
    html_file = TEST_DIR / "sample1.html"
    json_file = TEST_DIR / "sample1.json"

    # Load the expected output from the JSON file
    with open(json_file, "r") as h:
        expected_output = json.load(h)

    # Run the extractor on the HTML file and convert the result to a dictionary
    extracted_content = extractor.run(str(html_file)).model_dump()

    # Assert that the extracted content matches the expected output
    assert (
        extracted_content == expected_output
    ), "Extracted content does not match the expected output."
