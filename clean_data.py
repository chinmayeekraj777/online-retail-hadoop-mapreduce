import pandas as pd

input_file = "/home/chinmayee/online_retail/input/online_retail.csv"
output_file = "/home/chinmayee/online_retail/input/online_retail_clean.csv"

print("Loading dataset...")
df = pd.read_csv(input_file)

original_rows = len(df)

# Remove cancelled invoices
df = df[~df["InvoiceNo"].astype(str).str.startswith("C")].copy()

# Keep only positive quantities and prices
df = df[(df["Quantity"] > 0) & (df["UnitPrice"] > 0)].copy()

# Remove records without a product description
df = df[df["Description"].notna()].copy()
df = df[df["Description"].astype(str).str.strip() != ""].copy()

# Calculate revenue for each transaction line
df["Revenue"] = df["Quantity"] * df["UnitPrice"]

# Save the cleaned dataset
df.to_csv(output_file, index=False, encoding="utf-8")

print("\n===== CLEANING RESULTS =====")
print("Original rows:", original_rows)
print("Cleaned rows:", len(df))
print("Rows removed:", original_rows - len(df))
print("Unique countries:", df["Country"].nunique())
print("Unique products:", df["Description"].nunique())
print("Total quantity sold:", int(df["Quantity"].sum()))
print("Total sales revenue: £{:.2f}".format(df["Revenue"].sum()))

print("\nCleaned columns:")
print(df.columns.tolist())

print("\nFirst 5 cleaned records:")
print(df.head().to_string(index=False))

print("\nCleaned file saved to:")
print(output_file)
