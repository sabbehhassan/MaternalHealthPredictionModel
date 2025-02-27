from flask import Flask, request, jsonify
import pickle
import numpy as np
import pandas as pd
import os
import logging
from flask_cors import CORS

# ✅ Logging setup
logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)
CORS(app)  # Allow frontend to communicate with backend

# ✅ Model ka sahi path set karna
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(BASE_DIR, "models/maternal_health_model.pkl")

# ✅ Model ko load karna
try:
    with open(model_path, "rb") as file:
        model = pickle.load(file)
    print("✅ Model loaded successfully!")
except FileNotFoundError:
    logging.error(f"❌ Model file not found at {model_path}")
    model = None
except Exception as e:
    logging.error(f"❌ Error loading model: {e}")
    model = None

# ✅ API Home Route
@app.route('/')
def home():
    return "✅ Maternal Health Prediction API is running!"

# ✅ Prediction Route
@app.route('/predict', methods=['POST'])
def predict():
    try:
        print("📩 Request received:", request.json)  # Debugging ke liye

        if model is None:
            print("❌ Model not loaded properly")
            return jsonify({'error': 'Model not loaded properly'}), 500

        data = request.json

        # ✅ Correct Feature Names Mapping
        formatted_data = {
            "Age": data["age"],
            "SystolicBP": data["systolic_bp"],
            "DiastolicBP": data["diastolic_bp"],
            "BS": data["blood_sugar"],
            "BodyTemp": data["body_temp"],
            "HeartRate": data["heart_rate"]
        }

        # Convert JSON to DataFrame
        input_data = pd.DataFrame([formatted_data])

        # Ensure values are numeric
        input_data = input_data.apply(pd.to_numeric, errors='coerce')

        # Check for NaN values
        if input_data.isnull().values.any():
            print("❌ Invalid input values")
            return jsonify({"error": "Invalid input values, please check your data"}), 400

        # Predict using Model
        prediction = model.predict(input_data)[0]
        print("✅ Prediction successful:", prediction)

        return jsonify({'prediction': prediction})

    except Exception as e:
        print("❌ Error in prediction:", e)  # Yeh error terminal me print karega
        return jsonify({'error': str(e)}), 500

# ✅ Run Flask Server
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
