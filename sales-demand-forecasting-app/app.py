import streamlit as st
import pandas as pd
import plotly.express as px
import joblib

# Load model
rf = joblib.load("sales_rff.pkl")

# Load data
data = pd.read_csv("supermarket_sales.csv")


st.title("📊 Demand Forecasting Dashboard (Random Forest)")

products = data['Product_Name'].unique()
selected_product = st.selectbox("Select Product", products)

min_date = pd.to_datetime(data['Order_Date']).min().date()
max_date = pd.to_datetime(data['Order_Date']).max().date()

date_range = st.slider(
    "Select Date Range",
    min_value=min_date,
    max_value=max_date,
    value=(min_date, max_date)
)

# Filter data
filtered_data = data[(data['Product_Name'] == selected_product) &
                     (pd.to_datetime(data['Order_Date']).dt.date >= date_range[0]) &
                     (pd.to_datetime(data['Order_Date']).dt.date <= date_range[1])]

st.subheader(f"Forecast for {selected_product}")
st.write(filtered_data)

filtered_data['Year'] = pd.to_datetime(filtered_data['Order_Date']).dt.year
filtered_data['Month'] = pd.to_datetime(filtered_data['Order_Date']).dt.month
filtered_data['Day'] = pd.to_datetime(filtered_data['Order_Date']).dt.day

X_dashboard = pd.get_dummies(filtered_data[['Region', 'Product_Category', 'Deal_Size', 'Year', 'Month', 'Day']], drop_first=True)

for col in rf.feature_names_in_:
    if col not in X_dashboard.columns:
        X_dashboard[col] = 0
X_dashboard = X_dashboard[rf.feature_names_in_]

# Predict
y_pred = rf.predict(X_dashboard)
filtered_data['Forecast'] = y_pred

total_actual = filtered_data['Units_Sold'].sum()
total_forecast = filtered_data['Forecast'].sum()
perc_diff = ((total_forecast - total_actual) / total_actual) * 100 if total_actual != 0 else 0

st.metric(label="Total Actual Sales", value=int(total_actual))
st.metric(label="Total Forecasted Sales", value=int(total_forecast))
st.metric(label="% Difference", value=f"{perc_diff:.2f}%")

# Feature importance
st.subheader("Top Contributing Features")
feature_importances = pd.DataFrame({
    'Feature': X_dashboard.columns,
    'Importance': rf.feature_importances_
}).sort_values(by='Importance', ascending=False)
st.bar_chart(feature_importances.set_index('Feature'))

# chart
fig = px.line(filtered_data, x='Order_Date', y=['Units_Sold', 'Forecast'],
              labels={'value':'Units Sold', 'Order_Date':'Date'},
              title="Actual vs Forecast")
st.plotly_chart(fig)

st.download_button(
    label="Download Forecast CSV",
    data=filtered_data.to_csv(index=False),
    file_name=f"{selected_product}_forecast.csv",
    mime='text/csv'
)
