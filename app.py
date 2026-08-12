
import streamlit as st
import pandas as pd
import joblib

model = joblib.load("car_price_model.pkl")

st.set_page_config(
    page_title="Car Price Predictor",
    page_icon="🚗"
)

st.title("🚗 Car Price Prediction App")
st.write("Enter the details of a used car to estimate its selling price.")

year = st.number_input("Manufacturing Year", 1990, 2026, 2018)

km_driven = st.number_input(
    "Kilometres Driven",
    min_value=0,
    max_value=1000000,
    value=50000
)

fuel = st.selectbox(
    "Fuel Type",
    ["Diesel", "Petrol", "CNG", "LPG", "Electric"]
)

seller_type = st.selectbox(
    "Seller Type",
    ["Individual", "Dealer", "Trustmark Dealer"]
)

transmission = st.selectbox(
    "Transmission",
    ["Manual", "Automatic"]
)

owner = st.selectbox(
    "Owner",
    [
        "First Owner",
        "Second Owner",
        "Third Owner",
        "Fourth & Above Owner",
        "Test Drive Car"
    ]
)

mileage = st.number_input(
    "Mileage (km/ltr/kg)",
    min_value=0.0,
    max_value=100.0,
    value=19.44
)

engine = st.number_input(
    "Engine (CC)",
    min_value=0.0,
    max_value=10000.0,
    value=1248.0
)

max_power = st.number_input(
    "Max Power (bhp)",
    min_value=0.0,
    max_value=2000.0,
    value=81.83
)

seats = st.number_input(
    "Number of Seats",
    min_value=1,
    max_value=20,
    value=5
)

if st.button("Predict Car Price"):

    input_data = pd.DataFrame({
        "year": [year],
        "km_driven": [km_driven],
        "fuel": [fuel],
        "seller_type": [seller_type],
        "transmission": [transmission],
        "owner": [owner],
        "mileage(km/ltr/kg)": [mileage],
        "engine": [engine],
        "max_power": [max_power],
        "seats": [seats]
    })

    prediction = model.predict(input_data)[0]

    st.success(f"Estimated Selling Price: ₹{prediction:,.0f}")
