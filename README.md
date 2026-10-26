# Online Retail Sales Analysis Using Hadoop MapReduce

## 1. Project Overview
This project analyzes online retail transaction data using Apache Hadoop, HDFS, Hadoop Streaming, Python MapReduce, and an interactive Streamlit dashboard.

## 2. Dataset
Dataset: Online Retail
Source: UCI Machine Learning Repository
Link: https://archive.ics.uci.edu/dataset/352/online+retail

The original dataset contains 541,909 records and 8 columns. The original Excel file is approximately 23 MB. After cleaning, 530,104 records and 9 columns remain.

Dataset files are kept locally and are not uploaded to this repository. See input/README.md for dataset details.

## 3. Data Cleaning
The cleaning process excludes cancelled invoices, non-positive quantities, non-positive unit prices, and missing or blank product descriptions.

Revenue is calculated as:

Revenue = Quantity × UnitPrice

## 4. Hadoop MapReduce Workflow
1. Inspect the original dataset.
2. Convert the Excel dataset into CSV format.
3. Clean the transaction data.
4. Upload the processed data to HDFS.
5. Run the Python mapper and reducer using Hadoop Streaming.
6. Analyze the aggregated results.
7. Display the findings using charts and an interactive dashboard.

## 5. Key Results
- Cleaned transaction records: 530,104
- Total quantity sold: 5,588,376
- Total revenue: £10,666,684.54
- Countries represented: 38
- Unique product descriptions: 4,026
- MapReduce output records: 8,070

Revenue represents the value of retained transaction lines, not net profit.

## 6. Visualizations
- results/top_10_countries.png
- results/top_10_products.png

## 7. Interactive Dashboard
The Streamlit dashboard displays sales KPIs, country revenue analysis, product search, product revenue and quantity charts, and a top-N display slider.

## 8. Installation
Install the required Python packages:

pip install -r requirements.txt

## 9. Run the Dashboard
From the project directory, activate the virtual environment and start Streamlit:

source venv/bin/activate
streamlit run dashboard.py

The dashboard reads the aggregated data from results/mapreduce_output.txt.

## 10. Main Project Files
- inspect_data.py: Inspects the original dataset.
- convert_to_csv.py: Converts Excel data to CSV.
- clean_data.py: Cleans transaction data.
- mapper.py: Generates MapReduce key-value pairs.
- reducer.py: Aggregates values.
- visualize_results.py: Creates charts.
- dashboard.py: Runs the interactive dashboard.
- results/mapreduce_output.txt: Contains aggregated results.
- requirements.txt: Lists Python dependencies.
