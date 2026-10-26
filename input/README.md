# Dataset Information

## Dataset
UCI Online Retail Dataset

## Official Source
https://archive.ics.uci.edu/dataset/352/online+retail

## Original Dataset
- Original archive: online_retail.zip (approximately 23 MB)
- Extracted Excel file: Online Retail.xlsx (approximately 23 MB)
- Original records: 541,909
- Original columns: 8

## Project Data Files
- online_retail.csv: CSV converted from the original Excel file (approximately 46 MB)
- online_retail_clean.csv: cleaned dataset with the Revenue column (approximately 49 MB)
- online_retail_hadoop.csv: headerless CSV prepared for Hadoop MapReduce (approximately 49 MB)

## Cleaning
The cleaning process excludes cancelled invoices, non-positive quantities, non-positive unit prices, and rows with missing or blank descriptions.

- Cleaned records: 530,104
- Cleaned columns: 9
- Revenue: Quantity multiplied by UnitPrice

The dataset files are kept locally and are not included in this GitHub repository. Download the original dataset from the official UCI source above and follow the project scripts to reproduce the processing steps.
