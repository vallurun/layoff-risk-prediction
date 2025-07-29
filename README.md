# US Layoff Risk Prediction & Workforce Forecasting

This project uses regression-based machine learning to predict the likelihood of layoffs across industries and states. It combines predictive modeling, interactive dashboards, and a Flask-based API to enable proactive workforce decision-making.
---

##Features
- Trains a regression model to predict layoff risk based on industry and unemployment data  
- Includes a Jupyter notebook (`model_training.ipynb`) for data cleaning and model training  
- Sample dataset (`sample_data.csv`) with anonymized input features  
- A Flask API (`app.py`) that returns layoff risk scores for given input  
---

## 🔧 Tech Stack
- Python, Pandas, scikit-learn – Data processing and ML model  
- Flask – API backend for serving predictions  
- Jupyter Notebook – Model training and exploration  
- Power BI – Interactive visualization (dashboard.png optional)  
- Git + GitHub – Version control and project hosting
---

## Project Structure
layoff-risk-prediction/
├── app.py # Flask backend API
├── model_training.ipynb # Notebook for training the model
├── requirements.txt # Dependencies
├── sample_data.csv # Sample training dataset
├── README.md # Project documentation

---

## How to Run the Project

### 1. Clone the repository

git clone https://github.com/vallurun/layoff-risk-prediction.git
cd layoff-risk-prediction

**2. Install dependencies**

pip install -r requirements.txt

**3. Run the Flask app**

python app.py

**4. Make a POST request to the API**
Endpoint: http://localhost:5000/predict
Method: POST
Request Body Example (JSON):

{
  "industry_code": 12,
  "state_code": 6,
  "unemployment_rate": 4.5
}
Example Response:

{
  "layoff_risk_score": 0.68
}
