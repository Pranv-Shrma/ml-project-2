# to create a model 

from Network_Security.constants.training_pipeline import SAVED_MODEL_DIR, MODEL_FILE_NAME

import os
import sys
from Network_Security.exceptions.exception import NetworkSecurityException
from Network_Security.logging.logger import logging
from Network_Security.utils.main_utils.utils import load_object



class NetworkModel:
    def __init__(self, preprocessor,model):
        try:
            self.preprocessor = preprocessor
            self.model = model
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
    def predict(self, X):
        try:
            x_transform = self.preprocessor.transform(X)
            y_hat = self.model.predict(x_transform)
            return y_hat
        except Exception as e:
            raise NetworkSecurityException(e, sys) 



