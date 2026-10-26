import pandas as pd

input_file = "/home/chinmayee/online_retail/input/Online Retail.xlsx"
output_file = "/home/chinmayee/online_retail/input/online_retail.csv"

print("Reading Excel dataset...")
df = pd.read_excel(input_file, engine="openpyxl")

print("Converting Excel to CSV...")
df.to_csv(output_file, index=False, encoding="utf-8")

print("\nConversion successful!")
print("Dataset shape:", df.shape)
print("Columns:", df.columns.tolist())
print("\nFirst five records:")
print(df.head().to_string(index=False))
print("\nCSV saved to:", output_file)
