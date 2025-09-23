from pydantic import BaseModel , Field
from typing import Dict


class PredictionResponse(BaseModel):
    predicted_category :str= Field(..., description="The predicted Insurance Premiium Catrgory"),
    confidence:float = Field(..., description="Model's Confidence for the predicted class"),
    class_probabilities:Dict[str, float] = Field(..., description="Probability Distribution across all the classes ")
    