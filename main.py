from Network_Security.components.data_ingestion import DataIngestion
from Network_Security.components.data_validation import DataValidation, DataValidationConfig
from Network_Security.components.data_tranformation import DataTransformation, DataTransformationConfig
from Network_Security.logging.logger import logging
from Network_Security.exceptions.exception import NetworkSecurityException
from Network_Security.entity.config_entity import DataIngestionConfig, TrainingPipelineConfig, DataTransformationConfig, ModelTrainingConfig
from Network_Security.components.model_trainer import ModelTrainer

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
        data_transformation_config = DataTransformationConfig(trainingpipelineconfig)
        data_transformation = DataTransformation(data_validation_artifact, data_transformation_config)
        data_transformation_artifact = data_transformation.initiate_data_transformation()
        logging.info("Data transformation initiated.")
        print(data_transformation_artifact)
        logging.info("Data transformation completed.")

        logging.info("Model training initiated.")
        model_trainer_config = ModelTrainingConfig(trainingpipelineconfig)
        model_trainer = ModelTrainer(model_trainer_config, data_transformation_artifact)
        model_trainer_artifact = model_trainer.initiate_model_trainer()
        logging.info("Model training completed.")
        
    except Exception as e:
        raise NetworkSecurityException(e,sys)
