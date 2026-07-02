# Regular Expressions

Python `re` module examples.

| File | Description |
|------|-------------|
| [regexp.py](regexp.py) | Common regex patterns and examples |

## Common patterns
```python
import re

re.match(r'\d+', '123abc')     # match at start
re.search(r'\d+', 'abc123')    # search anywhere
re.findall(r'\d+', 'a1b2c3')   # all matches
re.sub(r'\s+', ' ', text)      # replace
re.split(r',\s*', 'a, b, c')   # split
```
