# this file is to load data from different sources: csv/ excel/ db/ apis/ cloud storage
# split dataset into train, validation, test sets

import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

# dataingestconfig is for the inputs

@dataclass
class DataIngestConfig:
    train_data_path : str = os.path.join('artifacts','train.csv')
    test_data_path : str = os.path.join('artifacts','test.csv')
    raw_data_path : str = os.path.join('artifacts','raw.csv')

class DataIngestion:
    def __init__(self):
        self.ingest_config = DataIngestConfig()
    def initiate_data_ingestion(self):
        logging.info('Implement data ingestion')
        try:
            # you can try read from db,...

            df = pd.read_csv('notebook\data\stud.csv')
            logging.info('load dataset as df')

            os.makedirs(os.path.dirname(self.ingest_config.train_data_path),
                        exist_ok = True)
            
            df.to_csv(self.ingest_config.raw_data_path, 
                      index = False,
                      header = True)
            
            logging.info('split raw !')

            train_set, test_set = train_test_split(df,
                                                   test_size=0.2,
                                                   random_state=36)
            
            train_set.to_csv(self.ingest_config.train_data_path,
                             index = False,
                             header = True)
            test_set.to_csv(self.ingest_config.test_data_path,
                             index = False,
                             header = True)
            logging.info('ingestion completed')

            return(
                self.ingest_config.train_data_path,
                self.ingest_config.test_data_path
            )

        except Exception as e:
            raise CustomException(e, sys)
    
if __name__ =="__main__":
    obj = DataIngestion()
    obj.initiate_data_ingestion()


