# 🌸 Iris Flower Classification – MLOps Project

## 📌 Project Overview
This project demonstrates **end-to-end ML deployment** using a trained Iris classification model.  
- The **ML model** predicts the species of an iris flower based on its sepal and petal measurements.  
- The **backend API** is built using **FastAPI** for high-performance inference.  
- The **frontend** is built using **Streamlit**, providing a **user-friendly interactive UI**.  
- Deployment is done on **Render**  for live usage.  

---

## 📂 Folder Structure

```


iris/
appfastapi/         # Backend - FastAPI API
main.py        # API code
model.pkl      # Trained ML model
requirements.txt
Dockerfile     # Optional Dockerfile for backend
appstreamlit/      # Frontend - Streamlit UI
app.py         # Streamlit app code
requirements.txt
.env           # Environment variable: API_URL
Dockerfile     # Optional Dockerfile for frontend
dockerfile-compose.yml
````

---

## ⚙️ Requirements

Install dependencies for backend and frontend separately:

### Backend
```bash
cd appfastapi
pip install -r requirements.txt
````

### Frontend

```bash
cd appstreamlit
pip install -r requirements.txt
pip install python-dotenv
```

---

## 🏃 Running Locally Without Docker

### 1️⃣ Backend (FastAPI)

```bash
cd appfastapi
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### 2️⃣ Frontend (Streamlit)

Set API URL in `.env` file:

```
API_URL=http://127.0.0.1:00/predict
```

Run Streamlit:

```bash
cd appstreamlit
streamlit run app.py
```

---

## 🐳 Running With Docker (Optional)

### 1️⃣ Backend Docker

**Dockerfile** in `appfastapi/` should have:

```dockerfile
FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

Build & Run:

```bash
cd appfastapi
docker build -t iris-backend .
docker run -p 8000:8000 iris-backend
```

### 2️⃣ Frontend Docker

**Dockerfile** in `appstreamlit/` should have:

```dockerfile
FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["streamlit", "run", "app.py", "--server.port", "8501", "--server.address", "0.0.0.0"]
```

Build & Run:

```bash
cd appstreamlit
docker build -t iris-frontend .
docker run -p 8501:8501 iris-frontend
```

### 3️⃣ Optional: docker-compose

Create `docker-compose.yml` in root:

```yaml
version: "3.8"
services:
  api:
    build: ./appfastapi
    ports:
      - "8000:8000"

  streamlit:
    build: ./appstreamlit
    ports:
      - "8501:8501"
    environment:
      - API_URL=http://api:8000/predict
    depends_on:
      - api
```

Run both containers:

```bash
docker-compose up --build
```

---

## ☁️ Deployment

### 1️⃣ Backend (Render)

* **Root Directory:** `appfastapi`
* **Build Command:** `pip install -r requirements.txt`
* **Start Command:** `uvicorn main:app --host 0.0.0.0 --port 10000`
* **Live URL Example:** `https://your-backend.onrender.com/predict`

### 2️⃣ Frontend (Hugging Face Spaces)

* **Root Directory:** `appstreamlit`
* **Environment Variable:**

```
API_URL=https://your-backend.onrender.com/predict
```

* Streamlit app fetches predictions from the deployed FastAPI backend.
* **Live URL Example:** `https:/.streamlit.app`

---

## 🔹 Features

* Enter sepal & petal measurements via **interactive sliders**.
* Get **predicted Iris species** instantly.
* **Probability charts** show prediction confidence for each species.
* Fully **environment-variable based**, flexible for cloud deployment.

---

## 🛠 Tools & Technologies

* **Python 3.10+**
* **FastAPI** – Backend API serving
* **Uvicorn** – ASGI server
* **Streamlit** – Frontend interactive UI
* **Render** – Cloud deployment of backend
* **Hugging Face Spaces** – Cloud deployment of frontend
* **Python-dotenv** – Load environment variables
* **Docker** – Containerize backend & frontend for portability

---

