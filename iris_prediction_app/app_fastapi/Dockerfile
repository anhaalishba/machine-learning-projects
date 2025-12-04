# FastAPI Dockerfile
FROM python:3.10

WORKDIR /app

# Copy only what API needs
COPY main.py best_pipeline.pkl requirements.txt ./

# Install dependencies
RUN pip install --no-cache-dir fastapi uvicorn pandas scikit-learn joblib

# Expose API port
EXPOSE 8000

# Run FastAPI
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
