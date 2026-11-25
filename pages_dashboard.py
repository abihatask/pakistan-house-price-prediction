import os

import pandas as pd
import plotly.express as px
import streamlit as st

FULL_FILE = "zameen-updated.csv"
SAMPLE_FILE = "data/zameen_sample.csv"


@st.cache_data
def load_data():
    cols = ["price", "city", "property_type", "bedrooms", "baths", "purpose", "Area Size"]
    # Use the full Kaggle file if it exists, otherwise the small sample from GitHub
    data_file = FULL_FILE if os.path.exists(FULL_FILE) else SAMPLE_FILE
    df = pd.read_csv(data_file, usecols=cols)
    df = df[df["purpose"].str.contains("sale", case=False, na=False)]
    return df


def show_home():
    st.title("Pakistan House Price Prediction")
    st.write(
        "This project predicts the price of a house in Pakistan using "
        "machine learning. It uses property data from Zameen.com."
    )
    st.info("Use the menu on the left to open the other pages.")


def show_data_overview():
    st.title("Data Overview")
    st.caption("Real property data from Zameen.com (Kaggle dataset).")
    df = load_data()

    col1, col2 = st.columns(2)
    col1.metric("Properties for sale", f"{len(df):,}")
    col2.metric("Cities", df["city"].nunique())

    st.subheader("Sample of the data")
    st.dataframe(df.head(20))

    st.subheader("Median price by city")
    city_price = df.groupby("city")["price"].median().reset_index()
    fig = px.bar(city_price, x="city", y="price")
    st.plotly_chart(fig)


def show_prediction():
    st.title("Predict House Price")
    df = load_data()

    city = st.selectbox("City", sorted(df["city"].unique()))
    prop_type = st.selectbox("Property type", sorted(df["property_type"].unique()))
    bedrooms = st.number_input("Bedrooms", min_value=0, max_value=20, value=3)
    baths = st.number_input("Bathrooms", min_value=0, max_value=20, value=2)
    area = st.number_input("Area size", min_value=1.0, value=5.0)

    if st.button("Predict"):
        # Simulated result. A real model comes in the final project.
        fake_price = area * 3_000_000 + bedrooms * 500_000 + baths * 300_000
        st.success(f"Estimated price: Rs {fake_price:,.0f}")
        st.caption("This is a simulated result. The real model will be added later.")


def show_dashboard(page):
    if page == "Home":
        show_home()
    elif page == "Data Overview":
        show_data_overview()
    elif page == "Prediction":
        show_prediction()