from fastapi import FastAPI
from fastapi.responses import JSONResponse
from model.predict import predict_output, model , MODEL_VERSION

from schema.user_input import UserInput

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to the Insurance Premium Prediction API. Use the /predict endpoint to get predictions."}
@app.get("/health")
def health_check():
    return {
            'status': 'ok',
            'version': MODEL_VERSION,
            'model_loaded': model is not None
        }

@app.post("/predict")
def predict_premium(input_data: UserInput):
    user_input = {
        "bmi": input_data.bmi,
        "age_group": input_data.age_group,
        "lifestyle_risk": input_data.lifestyle_risk,
        "city_tier": input_data.city_tier,
        "income_lpa": input_data.income_lpa,
        "occupation": input_data.occupation
    }

    prediction = predict_output(user_input)

    return JSONResponse(content={"predicted_insurance_premium_category": prediction})
