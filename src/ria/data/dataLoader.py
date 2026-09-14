import pandas as pd
from ria.config import CFG, RAW, INTERMEDIATE
import json


def get_business(gmap_id):
    return food[food["gmap_id"] == gmap_id]



meta = pd.read_json(RAW / CFG["data"]["meta"], lines=True)
meta = meta.dropna(subset=["category"])
cats = CFG["cleaning"]["food_keywords"]
# cats = ['restaurant', 'food', 'grill', 'chicken', 'pizza', 'burger', 'sandwich', 'steak', 'seafood', 'salad']
def is_food(category):
    category_flat = ' '.join(category).lower()
    for c in cats:
        if c in category_flat:
            return True
    return False
food = meta[meta["category"].apply(is_food)]

food.to_json(
    INTERMEDIATE / "meta_food.json",
    orient="records",
    lines=True,
    force_ascii=False,
)
food_ids = set(food["gmap_id"])
rows = []
foodies = 0
non_foodies = 0
with open(RAW / CFG["data"]["reviews"], encoding="utf-8") as f:
    for line in f:
        review = json.loads(line)
        if review["gmap_id"] in food_ids:
            foodies += 1
            rows.append(review)
        else:
            non_foodies += 1
reviews = pd.DataFrame(rows)
print(reviews.shape)
print(foodies, non_foodies)

reviews.to_json(
    INTERMEDIATE / "reviews_food.json",
    orient="records",
    lines=True,
    force_ascii=False,
)
