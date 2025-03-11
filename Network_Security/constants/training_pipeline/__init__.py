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

SCHEMA_FILE_PATH = os.path.join("Data_Schema", "schema.yaml")

'''
    Data Ingestion related constants, start with DATA_INGESTION
'''

DATA_INGESTION_COLLECTION_NAME : str = "Network_Data"
DATA_INGESTION_DATABASE_NAME : str = "Network_Security"
DATA_INGESTION_DIR_NAME : str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR : str = "feature_store"
DATA_INGESTION_INGESTED_DIR : str = "ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATION : float = 0.2


'''
    Data Validation related constants, start with DATA_VALIDATION
'''

DATA_VALIDATION_DIR_NAME : str = "Data_Validation"
DATA_VALIDATION_VALID_DIR : str = "Valid"
DATA_VALIDATION_INVALID_DIR : str = "Invalid"
DATA_VALIDATION_DRIFT_REPORT_DIR : str = "Drift_Report"
DATA_VALIDATION_DRIFT_REPORT_FILE_NAME : str = "drift_report.yaml"




