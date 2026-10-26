import pandas as pd

file_path = "/home/chinmayee/online_retail/input/online_retail.csv"

df = pd.read_csv(file_path)

print("===== DATASET INFORMATION =====")
print("Rows:", len(df))
print("Columns:", len(df.columns))
print("\nColumn names:")
print(df.columns.tolist())

print("\n===== MISSING VALUES =====")
print(df.isnull().sum())

print("\n===== CANCELLED INVOICES =====")
print("Cancelled invoice rows:",
      df["InvoiceNo"].astype(str).str.startswith("C").sum())

print("\n===== NEGATIVE QUANTITIES =====")
print("Rows with negative quantity:", (df["Quantity"] < 0).sum())

print("\n===== NEGATIVE PRICES =====")
print("Rows with negative price:", (df["UnitPrice"] < 0).sum())

print("\n===== SAMPLE RECORDS =====")
print(df.head(5).to_string(index=False))
