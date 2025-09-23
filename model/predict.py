import pandas as pd
import os
import pickle 

# Load model
model_path = os.path.join(os.path.dirname(__file__), "model.pkl")
with open(model_path, "rb") as f:
    model = pickle.load(f)
    
    #MLFlow
MODEL_VERSION = '1.0.0'

class_labels = model.classes_.tolist()


def predict_output(user_input: dict):
    input_df = pd.DataFrame([user_input])
    predicted_class = model.predict(input_df)[0]
    #Get probabilities for all the classes
    probabilities = model.predict_proba(input_df)[0]
    confidence =  max(probabilities)
    
    #creating mapping: {class_name: Probability}
    class_probs =dict(zip(class_labels, map(lambda p: round(p,4), probabilities)))
    
    return {
        'predicted_category':predicted_class,
        'confidence': round(confidence, 4),
        'class_probabilities': class_probs
    }
    