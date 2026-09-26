# 🍦 Ice Cream Sales Prediction & ML Pipeline

An end-to-end Machine Learning project that predicts daily ice cream sales revenue based on ambient weather parameters (Temperature & Humidity). Built with Python, Scikit-Learn, and Flask, containerized with Docker, and deployed on Hugging Face Spaces.

---

## 📊 Project Overview
* **Domain:** Retail & Sales Analytics / Demand Forecasting
* **Problem Type:** Supervised Continuous Regression
* **Input Features:** Temperature (°C), Relative Humidity (%)
* **Target Output:** Daily Sales Revenue ($)
* **Model Benchmark:** Linear Regression / Polynomial Features ($R^2 = 0.9441$, $\text{RMSE} = \$12.16$)

---

## 🏗️ Project Architecture & Directory Structure

```text
icecream_sales/
├── Dataset/                     # Raw weather and sales dataset (.csv)
├── Model Training Code/         # Jupyter notebook / training scripts
├── models/                      # Serialized ML model artifact (.pkl)
├── static/                      # CSS styling & static presentation assets
├── templates/                   # Flask HTML UI templates (index.html)
├── app.py                       # Flask application controller & routes
├── model.py                     # Model wrapper & pickle deserialization
├── util.py                      # Input validation & preprocessing helper functions
├── Dockerfile                   # Docker container specification (Port 7860)
├── requirements.txt             # Python dependencies
├── .gitignore                   # Git ignore settings
└── IceCream_Sales_ML_Pipeline_Presentation.pptx  # 20-slide PPT presentation deck

🚀 Local Setup & Installation
1. Clone the Repository
Bash
git clone [https://github.com/hammad544053/icecream-sales-ml-project.git](https://github.com/hammad544053/icecream-sales-ml-project.git)
cd icecream-sales-ml-project

2. Set Up Virtual Environment & Dependencies
Bash
# Create virtual environment
python -m venv venv

# Activate on Windows
venv\Scripts\activate

# Activate on macOS/Linux
source venv/bin/activate

# Install requirements
pip install -r requirements.txt

3. Run the Flask Web App Locally
Bash
python app.py
Open your browser and navigate to http://127.0.0.1:5000/.

🐳 Docker Support
To build and run the application container locally using Docker:

Bash
# Build Docker image
docker build -t icecream-sales-app .

# Run container on port 7860
docker run -p 7860:7860 icecream-sales-app
Then visit http://127.0.0.1:7860/ in your browser.
