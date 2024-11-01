from fastapi import FastAPI
import joblib
from routes import base , adherence
import logging
import os

app = FastAPI()

logger = logging.getLogger('uvivorn.error')

try:
    model_path = os.path.abspath("logistic_regression_model.joblib")
    model = joblib.load(model_path)
    logger.info(f"Model Loaded")
except Exception as e:
    logger.error(f"Error While loading the model : {e}")

app.include_router(base.base_router)
app.include_router(adherence.adherence_router)