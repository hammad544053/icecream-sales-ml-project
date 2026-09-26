# app.py - Main Flask Application for Ice Cream Sales Prediction

import os
from flask import Flask, request, render_template
from model import IceCreamPredictor
from util import validate_input, preprocess_input

app = Flask(__name__)

# Path to the saved model inside the 'models' directory
MODEL_PATH = os.path.join(os.path.dirname(__file__), 'models', 'best_sales_model.pkl')

# Load the machine learning model on app startup
try:
    predictor = IceCreamPredictor(model_path=MODEL_PATH)
    print("Model loaded successfully!")
except Exception as e:
    print(f"Error loading model: {e}")
    predictor = None


@app.route('/')
def home():
    """Display the home page with input form"""
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    """Process form submission and make sales prediction"""
    try:
        if predictor is None:
            return render_template('index.html',
                                   prediction_text="Error: Model not loaded. Check model file path.")

        # Extract values from form
        temperature = float(request.form['temperature'])
        humidity = float(request.form['humidity'])

        # Validate inputs using util.py
        is_valid, error_msg = validate_input(temperature, humidity)
        if not is_valid:
            return render_template('index.html',
                                   prediction_text=f"Error: {error_msg}",
                                   temperature=temperature,
                                   humidity=humidity)

        # Preprocess input features
        features = preprocess_input(temperature, humidity)

        # Make prediction
        predicted_sales = predictor.predict(features)
        result = f"Predicted Ice Cream Sales: ${predicted_sales:.2f}"

        return render_template('index.html',
                               prediction_text=result,
                               temperature=temperature,
                               humidity=humidity)

    except ValueError:
        return render_template('index.html',
                               prediction_text="Error: Please enter valid numbers for temperature and humidity.")
    except Exception as e:
        return render_template('index.html',
                               prediction_text=f"Error: {str(e)}")


if __name__ == '__main__':
    # Port 7860 is standard for Hugging Face Spaces (Docker / Flask SDK)
    port = int(os.environ.get("PORT", 7860))
    app.run(host='0.0.0.0', port=port, debug=True)