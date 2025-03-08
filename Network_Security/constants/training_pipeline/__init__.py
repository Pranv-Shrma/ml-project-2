import os
import sys
import numpy as np
import pandas as pd


'''
Defining common constants for training pipeline
'''

TARGET_COLUMN = "Result"
PIPELINE_NAME: str = "NetworkSecurity"
ARTIFACT_DIR: str = "Artifact"
FILE_NAME: str = "data.csv"

TRAIN_FILE_NAME: str = "train.csv"
TEST_FILE_NAME: str = "test.csv"



'''
    Data Ingestion related constants, start with DATA_INGESTION
'''

DATA_INGESTION_COLLECTION_NAME : str = "Network_Data"
DATA_INGESTION_DATABASE_NAME : str = "Network_Security"
DATA_INGESTION_DIR_NAME : str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR : str = "feature_store"
DATA_INGESTION_INGESTED_DIR : str = "ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATION : float = 0.2





