# Use official lightweight Python image
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    git \
    && rm -rf /var/lib/apt/lists/*

# Copy project files
COPY . /app

# Install Python dependencies
RUN pip install --upgrade pip

# You can replace `requirements.txt` with direct installs if needed
RUN pip install streamlit pandas torch transformers bert_score nltk scikit-learn

# Set Streamlit configuration (to suppress warnings)
ENV STREAMLIT_BROWSER_GATHER_USAGE_STATS=false

# Expose the port Streamlit runs on
EXPOSE 8501

# Run the app
CMD ["streamlit", "run", "app.py"]
