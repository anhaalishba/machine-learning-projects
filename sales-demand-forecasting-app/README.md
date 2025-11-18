# 📊 Sales Forcasting App

This project is an interactive **Demand Forecasting Dashboard** built using **Streamlit**, **Random Forest**, and **Plotly**.  
It allows users to filter products, select date ranges, visualize actual vs forecasted sales, and download forecast results.
Try:
https://forcastingsales.streamlit.app/
---

## 🚀 Features

- Product-wise demand forecasting  
- Date range filtering  
- Automatic feature engineering  
- Random Forest prediction  
- Feature importance visualization  
- Interactive line charts  
- Download forecast results as CSV  
- Clean and responsive Streamlit UI  

---

## 🧠 Model Used

- **Random Forest Regressor (sales_rf.pkl)**
- Trained on supermarket sales dataset
- Handles categorical + date features (via one-hot encoding)

---

## 📁 Project Structure

```

.
├── app.py                      # Main Streamlit app
├── sales_rff.pkl                # Trained ML model
├── supermarket_sales.csv       # Dataset
├── requirements.txt            # Project dependencies
└── README.md                   # Documentation

```

---

## ▶️ How to Run

1. Install dependencies:
```

pip install -r requirements.txt

```

2. Run Streamlit app:
```

streamlit run app.py


```

---

## 📦 Requirements

See `requirements.txt` file included in this repo.

---

## 📈 Output Preview

- Actual vs Forecast Graph  
- Feature Importance Chart  
- Forecast Table  
- Downloadable CSV  

---

## 🧑‍💻 Technologies Used

- **Python**
- **Streamlit**
- **Pandas**
- **Plotly Express**
- **Joblib**
- **Random Forest Regressor**

---

## 📥 Download Forecasts

The dashboard includes a built-in option to export filtered forecasts to CSV.

---

## 👩‍🔬 Author

**Anha Alishba**  
Machine Learning Practitioner

---
