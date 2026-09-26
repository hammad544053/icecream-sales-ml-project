# util.py

def preprocess_input(temp, humidity):
    """
    Preprocess features before prediction.
    Returns a 1D list [temp, humidity].
    """
    return [float(temp), float(humidity)]


def validate_input(temp, humidity):
    """
    Validate weather parameter ranges.
    """
    if not (-10 <= temp <= 50):
        return False, "Temperature must be between -10°C and 50°C"

    if not (0 <= humidity <= 100):
        return False, "Humidity must be between 0% and 100%"

    return True, ""