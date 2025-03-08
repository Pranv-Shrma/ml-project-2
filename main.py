from Network_Security.components.data_ingestion import DataIngestion
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
        print(dataingestionartifact)
        logging.info("Data ingestion completed.")
        
        
    except Exception as e:
        raise NetworkSecurityException(e,sys)
