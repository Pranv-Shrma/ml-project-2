from datetime import datetime
import os

from Network_Security.constants import training_pipeline

print(training_pipeline.DATA_INGESTION_COLLECTION_NAME)
print(training_pipeline.ARTIFACT_DIR)

class TrainingPipelineConfig:
    
    def __init__(self, timestamp=datetime.now()):
        timestamp = timestamp.strftime("%m_%d_%Y_%H_%M_%S")
        self.pipeline_name = training_pipeline.PIPELINE_NAME
        self.artifact_name = training_pipeline.ARTIFACT_DIR
        self.artifact_dir = os.path.join(self.artifact_name, timestamp)
        self.timestamp = timestamp
    
        
class DataIngestionConfig:
    """
    DataIngestionConfig is a configuration class that manages file paths and settings for the data ingestion process.
    
    This class provides a structured way to organize:
    - Directory paths for storing ingested data
    - File paths for feature store, training and testing datasets
    - Database connection details
    - Train-test split ratio
    
    Benefits:
    - Centralizes all data ingestion configuration in one place
    - Ensures consistent file organization across pipeline runs
    - Makes it easy to modify data ingestion parameters
    - Handles different operating system path separators (/ vs \)
    """
    def __init__(self,training_pipeline_config:TrainingPipelineConfig):
        self.data_ingestion_dir:str=os.path.join(
            training_pipeline_config.artifact_dir,training_pipeline.DATA_INGESTION_DIR_NAME
        )
        self.feature_store_file_path: str = os.path.join(
                self.data_ingestion_dir, training_pipeline.DATA_INGESTION_FEATURE_STORE_DIR, training_pipeline.FILE_NAME
            )
        self.training_file_path: str = os.path.join(
                self.data_ingestion_dir, training_pipeline.DATA_INGESTION_INGESTED_DIR, training_pipeline.TRAIN_FILE_NAME
            )
        self.testing_file_path: str = os.path.join(
                self.data_ingestion_dir, training_pipeline.DATA_INGESTION_INGESTED_DIR, training_pipeline.TEST_FILE_NAME
            )
        self.train_test_split_ratio: float = training_pipeline.DATA_INGESTION_TRAIN_TEST_SPLIT_RATION
        self.collection_name: str = training_pipeline.DATA_INGESTION_COLLECTION_NAME
        self.database_name: str = training_pipeline.DATA_INGESTION_DATABASE_NAME
