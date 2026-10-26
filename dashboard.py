
import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

# ---------------- PAGE CONFIGURATION ----------------
st.set_page_config(
    page_title="Online Retail Analytics",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Online Retail Sales Analytics Dashboard")
st.caption("Big Data Analytics | Hadoop MapReduce | Python | Streamlit")

# ---------------- LOAD MAPREDUCE RESULTS ----------------
file_path = Path("results/mapreduce_output.txt")

@st.cache_data
def load_results(path):
    countries = []
    products = []
    product_quantities = []
    total_revenue = 0.0
    total_quantity = 0.0

    with open(path, "r", encoding="utf-8") as file:
        for line in file:
            parts = line.rstrip("\n").split("\t", 1)
            if len(parts) != 2:
                continue

            key, raw_value = parts
            try:
                value = float(raw_value)
            except ValueError:
                continue

            if key == "TOTAL_REVENUE":
                total_revenue = value
            elif key == "TOTAL_QUANTITY":
                total_quantity = value
            elif key.startswith("COUNTRY_REVENUE|"):
                countries.append({
                    "Country": key.split("|", 1)[1],
                    "Revenue": value
                })
            elif key.startswith("PRODUCT_REVENUE|"):
                products.append({
                    "Product": key.split("|", 1)[1],
                    "Revenue": value
                })
            elif key.startswith("PRODUCT_QUANTITY|"):
                product_quantities.append({
                    "Product": key.split("|", 1)[1],
                    "Quantity": value
                })

    return (
        total_revenue,
        total_quantity,
        pd.DataFrame(countries),
        pd.DataFrame(products),
        pd.DataFrame(product_quantities)
    )

if not file_path.exists():
    st.error(f"Results file not found: {file_path}")
    st.info("Run the Hadoop MapReduce job and copy part-00000 into the results folder.")
    st.stop()

total_revenue, total_quantity, country_df, product_df, quantity_df = (
    load_results(str(file_path))
)

if country_df.empty or product_df.empty:
    st.error("Country or product results are missing from the MapReduce output.")
    st.stop()

# ---------------- SIDEBAR FILTERS ----------------
st.sidebar.header("Dashboard Filters")

country_options = ["All Countries"] + sorted(country_df["Country"].unique().tolist())
selected_country = st.sidebar.selectbox("Select Country", country_options)

search_text = st.sidebar.text_input("Search Product", placeholder="Enter product name")

top_n = st.sidebar.slider(
    "Number of items to display",
    min_value=5,
    max_value=20,
    value=10
)

# ---------------- KEY PERFORMANCE INDICATORS ----------------
st.subheader("Sales Overview")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Revenue", f"£{total_revenue:,.2f}")
col2.metric("Total Quantity Sold", f"{total_quantity:,.0f}")
col3.metric("Countries", f"{country_df['Country'].nunique()}")
col4.metric("Products", f"{product_df['Product'].nunique()}")

st.divider()

# ---------------- COUNTRY ANALYSIS ----------------
st.subheader("🌍 Country Revenue Analysis")

if selected_country == "All Countries":
    filtered_countries = country_df.copy()
else:
    filtered_countries = country_df[
        country_df["Country"] == selected_country
    ].copy()

country_chart_df = filtered_countries.nlargest(top_n, "Revenue").sort_values("Revenue")

fig_country = px.bar(
    country_chart_df,
    x="Revenue",
    y="Country",
    orientation="h",
    title=f"Revenue by Country (Top {top_n})",
    labels={"Revenue": "Revenue (£)", "Country": "Country"},
    color="Revenue",
    color_continuous_scale="Blues"
)
fig_country.update_layout(showlegend=False)
st.plotly_chart(fig_country, use_container_width=True)

st.dataframe(
    filtered_countries.sort_values("Revenue", ascending=False),
    use_container_width=True,
    hide_index=True
)

st.divider()

# ---------------- PRODUCT ANALYSIS ----------------
st.subheader("🛍️ Product Revenue Analysis")

filtered_products = product_df.copy()

if search_text.strip():
    filtered_products = filtered_products[
        filtered_products["Product"].str.contains(
            search_text.strip(), case=False, na=False, regex=False
        )
    ]

product_chart_df = (
    filtered_products.nlargest(top_n, "Revenue")
    .sort_values("Revenue")
)

if product_chart_df.empty:
    st.warning("No products match your search.")
else:
    fig_product = px.bar(
        product_chart_df,
        x="Revenue",
        y="Product",
        orientation="h",
        title=f"Products by Revenue (Top {top_n} matching products)",
        labels={"Revenue": "Revenue (£)", "Product": "Product"},
        color="Revenue",
        color_continuous_scale="Teal"
    )
    fig_product.update_layout(showlegend=False)
    st.plotly_chart(fig_product, use_container_width=True)

st.dataframe(
    filtered_products.sort_values("Revenue", ascending=False),
    use_container_width=True,
    hide_index=True
)

st.divider()

# ---------------- QUANTITY ANALYSIS ----------------
st.subheader("📦 Product Quantity Analysis")

if not quantity_df.empty:
    filtered_quantities = quantity_df.copy()

    if search_text.strip():
        filtered_quantities = filtered_quantities[
            filtered_quantities["Product"].str.contains(
                search_text.strip(), case=False, na=False, regex=False
            )
        ]

    quantity_chart_df = (
        filtered_quantities.nlargest(top_n, "Quantity")
        .sort_values("Quantity")
    )

    if not quantity_chart_df.empty:
        fig_quantity = px.bar(
            quantity_chart_df,
            x="Quantity",
            y="Product",
            orientation="h",
            title=f"Products by Quantity Sold (Top {top_n})",
            labels={"Quantity": "Quantity Sold", "Product": "Product"},
            color="Quantity",
            color_continuous_scale="Oranges"
        )
        fig_quantity.update_layout(showlegend=False)
        st.plotly_chart(fig_quantity, use_container_width=True)

# ---------------- PROJECT DETAILS ----------------
with st.expander("About this project"):
    st.write(
        "This dashboard visualizes aggregated results produced by a "
        "Hadoop Streaming MapReduce job on the cleaned Online Retail dataset."
    )
    st.write("**MapReduce output records:** 8,070")
    st.write("**Cleaned transaction records processed:** 530,104")
    st.write(
        "**Cleaning:** Cancelled invoices, non-positive quantities, "
        "non-positive unit prices, and missing or blank descriptions were excluded."
    )
    st.write(
        "**Important:** Revenue is calculated from retained transaction lines; "
        "it is not net profit."
    )

st.caption("Data source: UCI Online Retail dataset | Analysis: Hadoop MapReduce")
