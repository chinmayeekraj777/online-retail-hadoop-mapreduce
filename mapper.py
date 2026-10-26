#!/usr/bin/env python3
import sys
import csv

for line in sys.stdin:
    try:
        row = next(csv.reader([line]))

        if len(row) != 9:
            continue

        invoice, stock, description, quantity, date, price, customer, country, revenue = row

        quantity = float(quantity)
        revenue = float(revenue)

        print(f"TOTAL_REVENUE\t{revenue}")
        print(f"TOTAL_QUANTITY\t{quantity}")

        country = country.replace("\t", " ").strip()
        print(f"COUNTRY_REVENUE|{country}\t{revenue}")

        description = description.replace("\t", " ").strip()
        print(f"PRODUCT_REVENUE|{description}\t{revenue}")
        print(f"PRODUCT_QUANTITY|{description}\t{quantity}")

    except (ValueError, StopIteration, csv.Error):
        continue
