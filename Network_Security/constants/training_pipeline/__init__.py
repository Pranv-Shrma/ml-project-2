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


SAVED_MODEL_DIR = os.path.join("saved_models")
MODEL_FILE_NAME = "model.pkl"


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
PREPROCESSING_OBJECT_FILE_NAME : str = "preprocessing.pkl"


'''
    Data Transformation related constants, start with DATA_TRANSFORMATION
'''

DATA_TRANSFORMATION_DIR_NAME : str = "Data_Transformation"
DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR : str = "Transformed_Data"
DATA_TRANSFORMATION_TRANSFORMED_OBJECT_DIR : str = "Transformed_Object"


## knn imputer to fill missing/nan values
DATA_TRANSFORMATION_IMPUTER_PARAMS: dict = {
    "missing_values": np.nan,
    "n_neighbors": 3,
    "weights": "uniform"
}


'''
    Model Trainer related constants, start with MODEL_TRAINER
'''

MODEL_TRAINER_DIR_NAME : str = "Model_Trainer"
MODEL_TRAINER_TRAINED_MODEL_DIR : str = "Trained_Model"
MODEL_TRAINER_TRAINED_MODEL_NAME : str = "model.pkl"
MODEL_TRAINER_EXPECTED_SCORE : float = 0.6
MODEL_TRAINER_OVER_FITTING_UNDER_FITTING_THRESHOLD : float = 0.05







