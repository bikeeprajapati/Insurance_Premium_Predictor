import pandas as pd
import os
import pickle 

# Load model
model_path = os.path.join(os.path.dirname(__file__), "model.pkl")
with open(model_path, "rb") as f:
    model = pickle.load(f)
    
    #MLFlow
MODEL_VERSION = '1.0.0'


def predict_output(user_input: dict):
    input_df = pd.DataFrame([user_input])
    output = model.predict(input_df)[0]
    
    return output
    