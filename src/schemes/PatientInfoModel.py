from pydantic import BaseModel
from typing import Optional
class PatientInfoModel(BaseModel):

    disease_duration: float
    n_of_comorbidities: int
    sex: int  
    age: int
    residency: int
    education: int
    work: int
    finance: int
    n_of_hypertension_medication: int
    knowledge: int
    difficulty_medication: int
    medication_source: int
    distance_to_medication: int
    medication_price_affect: int
    phq2: int
    bmq1: int
