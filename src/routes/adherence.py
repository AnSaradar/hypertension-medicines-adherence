from fastapi import FastAPI, APIRouter, Depends, status ,Request
from fastapi.responses import JSONResponse
from preprocessing.Preprocessing import preprocess_input
from schemes.PatientInfoModel import PatientInfoModel
import os
import joblib
import logging

adherence_router = APIRouter(
    prefix="/api/v1/adherence",
    tags=["api_v1","adherence"],
)

logger = logging.getLogger('uvivorn.error')

@adherence_router.get("/predict")
async def predict(patient_data: PatientInfoModel):
    try:
        processed_data = preprocess_input(patient_data.dict())
        logger.error(f"processed_data shape:{processed_data.shape}")
    except Exception as e:
        logger.error(f"Error While preprocessing the data file : {e}")
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST,
                            content={
                                    "signal" : "Error While Prepcessing the data",
                                        
                        })
    
    try:
        joblib_in = open("logistic_regression_model.joblib","rb")
        model=joblib.load(joblib_in)
    except Exception as e:
        logger.error(f"Error While loading the model : {e}")
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST,
                            content={
                                    "signal" : "Error while loading the model",
                                        
                        })
    
    try:
        prediction = model.predict(processed_data)
        prediction_proba = model.predict_proba(processed_data)[:, 1]

        prediction_class = "The Patient will have a high Adherence to Hypertension medciens" if prediction[0] == 1 else "The Patient will have a low Adherence to Hypertension medciens"

        return JSONResponse(status_code=status.status.HTTP_200_OK,
                                    content={
                                            "Prediction Class" : prediction_class,
                                            "Prediction Probability" : prediction_proba[0],
                                                
                                }) 
    except Exception as e:
        logger.error(f"Error While predicting : {e}")
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST,
                            content={
                                    "signal" : "Error While predicting",
                                        
                        })    