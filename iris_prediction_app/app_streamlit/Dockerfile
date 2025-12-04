# Streamlit Dockerfile
FROM python:3.10

WORKDIR /app

# Copy Streamlit app
COPY app.py requirements.txt ./

# Install dependencies
RUN pip install --no-cache-dir streamlit requests pandas matplotlib seaborn

# Expose Streamlit port
EXPOSE 8501

# Run Streamlit
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
