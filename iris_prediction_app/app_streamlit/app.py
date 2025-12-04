import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Iris Flower Classifier 🌸")

st.title("Iris Flower Classification 🌸")
st.write("Enter the flower measurements below and see the predicted species along with charts.")

# -------------------------
# API URL Input
# -------------------------
API_URL = "http://127.0.0.1:8000/predict"
# -------------------------
# User Inputs
# -------------------------
with st.form("iris_form"):
    sepal_length = st.number_input("Sepal Length (cm)", min_value=0.0, max_value=10.0, value=5.1)
    sepal_width = st.number_input("Sepal Width (cm)", min_value=0.0, max_value=10.0, value=3.5)
    petal_length = st.number_input("Petal Length (cm)", min_value=0.0, max_value=10.0, value=1.4)
    petal_width = st.number_input("Petal Width (cm)", min_value=0.0, max_value=10.0, value=0.2)
    submitted = st.form_submit_button("Predict")

if submitted:
    payload = {
        "SepalLengthCm": sepal_length,
        "SepalWidthCm": sepal_width,
        "PetalLengthCm": petal_length,
        "PetalWidthCm": petal_width
    }

    try:
        response = requests.post(API_URL, json=payload)
        data = response.json()

        if response.status_code == 200:
            prediction = data['prediction']
            st.success(f"Predicted Species: **{prediction}**")

            # -------------------------
            # Probability Charts
            # -------------------------
            if 'probabilities' in data and data['probabilities']:
                st.subheader("Prediction Probabilities 📊")
                prob_df = pd.DataFrame.from_dict(data['probabilities'], orient='index', columns=['Probability'])
                st.bar_chart(prob_df)

            
        else:
            st.error(f"API Error: {data.get('detail', 'Unknown error')}")

    except Exception as e:
        st.error(f"Error connecting to API: {e}")
