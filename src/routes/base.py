from fastapi import FastAPI, APIRouter, Depends
import os

base_router = APIRouter(
    prefix="/api/v1",
    tags=["api_v1"],
)

@base_router.get("/")
async def welcome():
    app_name = "Medicens Adherence for Hypertension Patients"
    app_version = "0.1"

    return {
        "app_name": app_name,
        "app_version": app_version,
    }