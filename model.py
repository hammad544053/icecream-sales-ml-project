# model.py

import os
import pickle
import numpy as np


class IceCreamPredictor:
    """
    Class to handle model loading and prediction for ice cream sales.
    """

    def __init__(self, model_path=None):
        if model_path is None:
            model_path = os.path.join(os.path.dirname(__file__), 'models', 'best_sales_model.pkl')

        self.model_path = model_path
        self.model = self._load_model()

    def _load_model(self):
        try:
            with open(self.model_path, 'rb') as file:
                model = pickle.load(file)
            print(f"Model loaded from: {self.model_path}")
            return model
        except FileNotFoundError:
            print(f"Error: Model file '{self.model_path}' not found!")
            raise
        except Exception as e:
            print(f"Error loading model: {e}")
            raise

    def predict(self, features):
        """
        Predict sales based on features.
        Accepts list/array: [temperature, humidity] or 2D array [[temp, humidity]]
        """
        features_array = np.array(features)

        # Ensure 2D array format for scikit-learn
        if features_array.ndim == 1:
            features_array = features_array.reshape(1, -1)

        prediction = self.model.predict(features_array)
        return float(prediction[0])


if __name__ == "__main__":
    try:
        predictor = IceCreamPredictor()
        test_cases = [
            [30.0, 50.0],
            [25.0, 60.0],
            [35.0, 40.0],
            [15.0, 80.0]
        ]

        print("\n--- Running Model Tests ---")
        for i, sample in enumerate(test_cases):
            pred = predictor.predict(sample)
            print(f"Test {i + 1} | Temp: {sample[0]}°C, Humidity: {sample[1]}% => Predicted Sales: ${pred:.2f}")

    except Exception as e:
        print(f"Test failed: {e}")