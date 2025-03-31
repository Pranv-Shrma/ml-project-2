import sys, os
import numpy as np
import pandas as pd
from sklearn.impute import KNNImputer
from sklearn.pipeline import Pipeline


from Network_Security.constants.training_pipeline import TARGET_COLUMN
from Network_Security.constants.training_pipeline import DATA_TRANSFORMATION_IMPUTER_PARAMS

from Network_Security.entity.artifact_entity import DataTransformationArtifact, DataValidationArtifact
from Network_Security.entity.config_entity import DataTransformationConfig
from Network_Security.logging.logger import logging
from Network_Security.exceptions.exception import NetworkSecurityException
from Network_Security.utils.main_utils.utils import save_object, save_numpy_array_data

class DataTransformation:
    def __init__(self, data_validation_artifact: DataValidationArtifact, data_transformation_config: DataTransformationConfig):
        try:
            self.data_validation_artifact: DataValidationArtifact = data_validation_artifact
            self.data_transformation_config: DataTransformationConfig = data_transformation_config
            
        except Exception as e:
            raise NetworkSecurityException(e, sys)
    
    @staticmethod
    def read_data(file_path: str) -> pd.DataFrame:
        try:
            return pd.read_csv(file_path)
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
        
    def get_data_transformer_object(cls)->Pipeline:
        """
        It initialises a KNNImputer object with the parameters specified in the training_pipeline.py file
        and returns a Pipeline object with the KNNImputer object as the first step.

        Args:
          cls: DataTransformation

        Returns:
          A Pipeline object
        """
        logging.info(
            "Entered get_data_trnasformer_object method of Trnasformation class"
        )
        try:
           imputer:KNNImputer=KNNImputer(**DATA_TRANSFORMATION_IMPUTER_PARAMS)
           logging.info(
                f"Initialise KNNImputer with {DATA_TRANSFORMATION_IMPUTER_PARAMS}"
            )
           processor:Pipeline=Pipeline([("imputer",imputer)])
           return processor
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
        
    def initiate_data_transformation(self) -> DataTransformationArtifact:
        logging.info("Entered initiate_data_transformation method of DataTransformation class")
        try:
            logging.info("Starting data transformation")
            train_df = DataTransformation.read_data(self.data_validation_artifact.valid_test_file_path)
            test_df = DataTransformation.read_data(self.data_validation_artifact.valid_test_file_path)
            
            # training dataframe
            input_feature_train_df = train_df.drop(columns=[TARGET_COLUMN], axis=1)
            target_feature_train_df = train_df[TARGET_COLUMN]
            # replacing -1 with 0 in target column
            target_feature_train_df = target_feature_train_df.replace(-1,0)
            
            # test dataframe
            input_feature_test_df = test_df.drop(columns=[TARGET_COLUMN], axis=1)
            target_feature_test_df = test_df[TARGET_COLUMN]
            # replacing -1 with 0 in target column
            target_feature_test_df = target_feature_test_df.replace(-1,0)
            
            
            preprocessor = self.get_data_transformer_object()
            
            preprocessor_object = preprocessor.fit(input_feature_train_df)
            transformerd_input_train_feature = preprocessor.transform(input_feature_train_df)
            transformerd_input_test_feature = preprocessor.transform(input_feature_test_df)
            
            train_arr = np.c_[transformerd_input_train_feature, np.array(target_feature_train_df)]
            test_arr = np.c_[transformerd_input_test_feature, np.array(target_feature_test_df)]
            
            # save numpy array data
            save_numpy_array_data(self.data_transformation_config.transformed_train_file_path, train_arr)
            save_numpy_array_data(self.data_transformation_config.transformed_test_file_path, test_arr)
            
            # save preprocessor object
            save_object(self.data_transformation_config.transformed_object_file_path, preprocessor_object)
            
            
            # prepare artifacts
            data_transformation_artifact = DataTransformationArtifact(
                transformed_object_file_path=self.data_transformation_config.transformed_object_file_path,
                transformed_train_file_path=self.data_transformation_config.transformed_train_file_path,
                transformed_test_file_path=self.data_transformation_config.transformed_test_file_path
            )
            
            
            return data_transformation_artifact
            
        except Exception as e:
            raise NetworkSecurityException(e, sys) from e
        
        
        
        




