# Install locally

```bash
cd lovesoup
ls

# Output
lovesoup
pyproject.toml
README.md
```

```bash
pip install -e .
# Output
Audited 1 package in 10ms
```

# Usage
```python

from lovesoup.post_processing import BatDongSan, Cenhomes, BDS123Vn, Mogi, Muabannet, Nhatot

extractor = Muabannet()

extractor.run_html(html_str)
extractor.run(path_to_html)
```

