import os
import pandas as pd

df = pd.read_csv("zameen-updated.csv")
df = df[df["purpose"].str.contains("sale", case=False, na=False)]

cols = ["price", "city", "location", "property_type", "bedrooms",
        "baths", "Area Size", "Area Type", "Area Category", "purpose"]
sample = df[cols].sample(5000, random_state=42)

os.makedirs("data", exist_ok=True)
sample.to_csv("data/zameen_sample.csv", index=False)
print("Done:", sample.shape)