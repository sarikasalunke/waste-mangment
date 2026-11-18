import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("waste_model.pkl")

st.title("♻️ Waste Classification System")

st.write("Enter waste details to predict the waste type.")

weight = st.number_input(
    "Weight (grams)",
    min_value=0.0,
    value=200.0
)

moisture = st.number_input(
    "Moisture (%)",
    min_value=0.0,
    max_value=100.0,
    value=20.0
)

recyclable = st.selectbox(
    "Is it recyclable?",
    ["Yes", "No"]
)

recyclable_value = 1 if recyclable == "Yes" else 0

if st.button("Predict Waste Type"):

    data = pd.DataFrame({
        "weight_grams": [weight],
        "moisture_percent": [moisture],
        "recyclable": [recyclable_value]
    })

    prediction = model.predict(data)

    st.success(
        f"Predicted Waste Type: {prediction[0]}"
    )