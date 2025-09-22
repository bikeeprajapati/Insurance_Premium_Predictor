from pydantic import BaseModel, Field, computed_field
from typing import Literal, Annotated
from config.city_tier import tier_1_cities, tier_2_cities

#Pydantic model with computed fields inside the class
# Modify city field in Pydantic model
class UserInput(BaseModel):
    age: Annotated[int, Field(..., gt=0, lt=120, description="Age must be between 1 and 119")]
    weight: Annotated[float, Field(..., gt=0, lt=500, description="Weight must be between 1 and 499")]
    height: Annotated[float, Field(..., gt=0, lt=300, description="Height must be between 1 and 299")]
    income_lpa: Annotated[float, Field(..., gt=0, lt=1000, description="Income must be between 1 and 999")]
    smoker: Annotated[Literal["yes", "no"], Field(..., description="Smoker must be either 'yes' or 'no'")]
    city: Annotated[str, Field(..., description="Enter your city name")]
    occupation: Annotated[
        Literal["retired", "freelancer", "student", "government_job",
                "business_owner", "unemployed", "private_job"],
        Field(..., description="Occupation must be one of the allowed categories")
    ]
    
    

    @computed_field
    @property
    def bmi(self) -> float:
        return round(self.weight / (self.height ** 2), 2)

    @computed_field
    @property
    def lifestyle_risk(self) -> str:
        if self.smoker == "yes" and self.bmi > 30:
            return "high"
        elif self.smoker == "yes" and self.bmi > 27:
            return "medium"
        return "low"

    @computed_field
    @property
    def city_tier(self) -> int:
        city_clean = self.city.strip().title()  # normalize input
        if city_clean in tier_1_cities:
            return 1
        elif city_clean in tier_2_cities:
            return 2
        else:
            return 3  # default to tier_3 if not found

    @computed_field
    @property
    def age_group(self) -> str:
        if self.age < 25:
            return "young"
        elif self.age < 45:
            return "adult"
        elif self.age < 60:
            return "middle_aged"
        return "senior"
