from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np

app = Flask(__name__)

# Load trained model
model = pickle.load(open('layoff_model.pkl', 'rb'))

@app.route('/')
def home():
    return "Layoff Risk Prediction API is Running"

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        input_features = [
            float(data['industry_code']),
            float(data['state_code']),
            float(data['unemployment_rate'])
        ]
        prediction = model.predict([input_features])
        return jsonify({'layoff_risk_score': round(prediction[0], 2)})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == "__main__":
    app.run(debug=True)
