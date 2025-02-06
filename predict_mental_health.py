
import joblib
import pandas as pd
import sys

# Load the model
model = joblib.load('mental_health_model.pkl')

# Example input
input_data = pd.DataFrame([sys.argv[1:]], columns=[...])  # Specify column names

# Predict
prediction = model.predict(input_data)
print("Predicted Mental Health Condition:", prediction)
