# technically the frontend of our application

import sys
import os
import certifi

ca = certifi.where()

from dotenv import load_dotenv
load_dotenv()

mongo_db_url = os.getenv("MONGO_DB_URL")

import pymongo
from Network_Security.logging.logger import logging
from Network_Security.exceptions.exception import NetworkSecurityException
from Network_Security.pipeline.training_pipeline import TrainingPipeline
# from Network_Security.utils.main_utils import load_object

from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, File, UploadFile, Request
from uvicorn import run as app_run
from fastapi.responses import Response
from starlette.responses import RedirectResponse
import pandas as pd

client = pymongo.MongoClient(mongo_db_url, tlsCAFile=ca)

from Network_Security.constants.training_pipeline import DATA_INGESTION_COLLECTION_NAME
from Network_Security.constants.training_pipeline import DATA_INGESTION_DATABASE_NAME

database = client[DATA_INGESTION_DATABASE_NAME]
collection = database[DATA_INGESTION_COLLECTION_NAME]



app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", tags=["authentication"])
async def index():
    return RedirectResponse(url="/docs")

@app.get("/train")
async def train_route():
    try:
        training_pipeline = TrainingPipeline()
        training_pipeline.run_pipeline()
        return Response("Training successful !!")
    except Exception as e:
        raise NetworkSecurityException(e,sys)
    
@app.get("/predict")
async def predict_route():
    try:
        pass
    except Exception as e:
        raise NetworkSecurityException(e,sys)
    
if __name__ == "__main__":
    app_run(app, host="localhost", port=8000)


