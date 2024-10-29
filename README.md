# Installation

```bash
$ git clone https://github.com/xtfocus/bds_rule_based_scraping.git
$ cd bds_rule_based_scraping
$ ls
# Output
# lovesoup
# pyproject.toml
# README.md

$ pip install -e .
# Output
# Audited 1 package in 10ms
```

# Usage

```python
from lovesoup.cooks import BatDongSan, Cenhomes, BDS123Vn, Mogi, Muabannet, Nhatot

muabannet_extractor = Muabannet()

muabannet_extractor.kun_html(html_str) # html_str is a muaban.net ad site HTML string 
# or
muabannet_extractor.run(path_to_html)
# Just the images from the ad:
muabannet_extractor.run_html(html_str).images
```


