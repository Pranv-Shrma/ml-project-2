from Network_Security.components.data_ingestion import DataIngestion
from Network_Security.components.data_validation import DataValidation, DataValidationConfig
from Network_Security.logging.logger import logging
from Network_Security.exceptions.exception import NetworkSecurityException
from Network_Security.entity.config_entity import DataIngestionConfig
from Network_Security.entity.config_entity import TrainingPipelineConfig


import sys

if __name__ == "__main__":
    try:
        trainingpipelineconfig = TrainingPipelineConfig()
        dataingestionconfig = DataIngestionConfig(trainingpipelineconfig)
        data_ingestion = DataIngestion(dataingestionconfig)
        logging.info("Data ingestion initiated.")
        dataingestionartifact = data_ingestion.initiate_data_ingestion()
        logging.info("Data ingestion completed.")
        print(dataingestionartifact)
        data_validation_config = DataValidationConfig(trainingpipelineconfig)
        data_validaton = DataValidation(dataingestionartifact, data_validation_config)
        logging.info("Data validation initiated.")
        data_validation_artifact = data_validaton.initiate_data_validation()
        logging.info("Data validation completed.")
        print(data_validation_artifact)

        
    except Exception as e:
        raise NetworkSecurityException(e,sys)
