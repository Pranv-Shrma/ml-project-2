import os
import sys
import json
from dotenv import load_dotenv
load_dotenv()

from pymongo.mongo_client import MongoClient

MONGO_DB_URL = os.getenv("MONGO_DB_URL")

import certifi

ca = certifi.where() # provides a set of root certificates
# just to ensure we using valid requests


import pandas as pd
import numpy as np
import pymongo
from Network_Security.exceptions.exception import NetworkSecurityException
from Network_Security.logging.logger import logging


class NetworkDataExtract():
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def csv_to_json(self,file_path:str):
        try:
            data = pd.read_csv(file_path)
            data.reset_index(drop=True,inplace=True)  # since an automatic index is applied to the csv file
            records = list(json.loads(data.T.to_json()).values())
            return records
        except Exception as e:
            raise NetworkSecurityException(e,sys)

    def insert_data_mongodb(self,records,database,collection):
        try:
            self.database = database
            self.collection = collection
            self.records = records
            
            self.mongo_client = pymongo.MongoClient(MONGO_DB_URL)
            self.database = self.mongo_client[self.database]
            
            self.collection = self.database[self.collection]
            self.collection.insert_many(self.records)
            
            return (len(self.records))
            
        except Exception as e:
            raise NetworkSecurityException(e,sys)


if __name__ == "__main__":
    FILE_PATH = "Data\data.csv"
    DATABASE = "Network_Security"
    Collection = "Network_Data"
    
    networkObj = NetworkDataExtract()
    records = networkObj.csv_to_json(FILE_PATH)
    print(records)
    no_of_record = networkObj.insert_data_mongodb(records,DATABASE,Collection)
    print(no_of_record) 
    # logging.info(f"Data inserted successfully into the database {DATABASE} and collection {Collection} with {no_of_record} records")
        
            





