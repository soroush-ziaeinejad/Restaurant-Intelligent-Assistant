import json
from itertools import islice

with open("data/raw/review-Mississippi_10.json", encoding="utf-8") as f:
    for line in islice(f, 3):
        print(json.dumps(json.loads(line), indent=5, ensure_ascii=False))
