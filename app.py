import joblib
import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime

# Load base input columns
base_input = joblib.load("models/base_input.pkl")

@st.cache_resource
def load_models():
    try:
        lin_model = joblib.load("models/lin_pipeline.pkl")
        rf_model = joblib.load("models/rf_pipeline.pkl")
        return lin_model, rf_model
    except FileNotFoundError:
        st.error("Model files not found. Please check the models directory.")
        return None, None

lin_model, rf_model = load_models()

st.set_page_config(page_title="House Price Predictor", page_icon="🏠", layout="wide")

st.title("🏠 House Price Predictor")
st.markdown("*Predict house prices using Linear Regression or Random Forest models*")

col1, col2 = st.columns([1, 2])
with col1:
    model_choice = st.selectbox("Choose Model", ["Linear Regression", "Random Forest"])

st.header("📊 Input House Features")

col1, col2, col3 = st.columns(3)

with col1:
    lot_area = st.number_input("Lot Area (sq ft)", 
                              min_value=100, 
                              max_value=100000, 
                              value=8000,
                              help="Total lot size in square feet")

with col2:
    current_year = datetime.now().year
    year_built = st.slider("Year Built", 
                          min_value=1872, 
                          max_value=current_year, 
                          value=2005,
                          help="Year the house was built")

with col3:
    overall_qual = st.selectbox("Overall Quality", 
                               list(range(1, 11)),
                               index=4,
                               help="Overall quality rating (1=worst, 10=best)")

house_age = current_year - year_built

# Create raw input data
input_data_raw = pd.DataFrame([{
    "Lot Area": lot_area,
    "Year Built": year_built,
    "Overall Qual": overall_qual
}])

# Match input columns to training data
input_data = input_data_raw.reindex(columns=base_input().columns, fill_value=0)


st.subheader("📋 Input Summary")
col1, col2, col3, col4 = st.columns(4)
col1.metric("Lot Area", f"{lot_area:,} sq ft")
col2.metric("Year Built", year_built)
col3.metric("House Age", f"{house_age} years")
col4.metric("Quality Rating", f"{overall_qual}/10")

if st.button("🔮 Predict Price", type="primary"):
    if lin_model and rf_model:
        if model_choice == "Linear Regression":
            price = lin_model.predict(input_data)[0]
        else:
            price = rf_model.predict(input_data)[0]
        
        st.success(f"💰 Predicted House Price: **${price:,.0f}**")
        
        price_range = price * 0.1
        st.info(f"📊 Estimated range: ${price - price_range:,.0f} - ${price + price_range:,.0f}")
        
        fig = go.Figure()
        fig.add_trace(go.Indicator(
            mode="number+delta",
            value=price,
            number={'prefix': "$", 'valueformat': ",.0f"},
            delta={'reference': price - price_range, 'relative': False},
            title={"text": "Predicted Price"},
            domain={'x': [0, 1], 'y': [0, 1]}
        ))
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.error("⚠️ Models not loaded properly.")
