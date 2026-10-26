import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt
from pathlib import Path

input_file = Path("results/mapreduce_output.txt")
countries = {}
products = {}

with input_file.open(encoding="utf-8") as f:
    for line in f:
        parts = line.rstrip("\n").split("\t", 1)

        if len(parts) != 2:
            continue

        key, value = parts

        try:
            value = float(value)
        except ValueError:
            continue

        if key.startswith("COUNTRY_REVENUE|"):
            name = key.split("|", 1)[1]
            countries[name] = value

        elif key.startswith("PRODUCT_REVENUE|"):
            name = key.split("|", 1)[1]
            products[name] = value

Path("results").mkdir(exist_ok=True)

# Chart 1: Top 10 countries
top_countries = sorted(
    countries.items(), key=lambda item: item[1], reverse=True
)[:10]
top_countries.reverse()

plt.figure(figsize=(11, 7))
plt.barh(
    [x[0] for x in top_countries],
    [x[1] for x in top_countries]
)
plt.xlabel("Sales Revenue (£)")
plt.ylabel("Country")
plt.title("Top 10 Countries by Sales Revenue")
plt.tight_layout()
plt.savefig("results/top_10_countries.png", dpi=200)
plt.close()

# Chart 2: Top 10 products
top_products = sorted(
    products.items(), key=lambda item: item[1], reverse=True
)[:10]
top_products.reverse()

plt.figure(figsize=(12, 8))
plt.barh(
    [x[0] for x in top_products],
    [x[1] for x in top_products]
)
plt.xlabel("Sales Revenue (£)")
plt.ylabel("Product")
plt.title("Top 10 Products by Sales Revenue")
plt.tight_layout()
plt.savefig("results/top_10_products.png", dpi=200)
plt.close()

print("Visualizations created successfully!")
print("Countries chart: results/top_10_countries.png")
print("Products chart: results/top_10_products.png")
