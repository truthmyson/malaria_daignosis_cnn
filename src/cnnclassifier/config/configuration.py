#  this will return the configuration values and needed params following the strict return type in entity/__init__.py

import os
from cnnclassifier.constants import *
from cnnclassifier import logger
from cnnclassifier.utils.common import read_yaml, create_directory
from cnnclassifier.entity.config_entity import (
    DataIngestionConfig,
    SplitDatasets,
    Preprocessing,
    BUildModel
)


# this will manage all the configurations for all operations in the projects
class configManager:
    def __init__(self,
                 config_file_path= CONFIG_FILE_PATH,
                 params_file_path= PARAMS_FILE_PATH
                 ):
        """
        It would read the yaml files and store the contents in config and params and then iitialise the artifcts directory
        Args
            config_file_path (str): path to the config.yaml file
            params_file_path (str): path to the params.yaml file
        """
                 
        self.config = read_yaml(config_file_path) # read the content of the config.yaml file
        self.params = read_yaml(params_file_path) # read the content of the params.yaml file

        # create the artifacts directory
        create_directory([self.config.artifacts_dir])


    def get_data_ingestion_config_params(self) -> DataIngestionConfig:
        """
        get the configuation and paramsfor data ingestion
        Args:
            none
        Returns: 
            DataIngestionConfig: return the structure of data ingestion config entity
        """
        config = self.config.data_ingestion # get all the confguration related to data ingestion
        params = self.params.data_ingestion_params # get all the params related to data ingestion

        create_directory([config.root_dir]) # create directory for data ingestion data

        data_ingestion_config_params = DataIngestionConfig(
            root_dir=config.root_dir,
            dataset_path=config.dataset_path,
            dataset_info_path=config.dataset_info_path,
            shuffle = params.shuffle,
            with_info = params.with_info,
            dataset_name = params.dataset_name,
            as_supervised = params.as_supervised,
            split = params.split
        )

        logger.info(f"Data ingestion configuration and params loaded successfully.")

        return data_ingestion_config_params
    

    def get_split_datasets_config_params(self) -> SplitDatasets:
        """
        get the configuration and params for data splitting
        Args:
            none
        Returns: 
            SplitDatasets: return the structure of data splitting config entity
        """
        config = self.config.split_dataset # get all the configuration related to data splitting
        params = self.params.split_datasets_params #get all the params related to data splitting

        create_directory([config.root_dir]) # create the directory for splitting data

        splitting_dataset_config_params = SplitDatasets(
            train_size = params.train_size,
            test_size = params.test_size,
            validation_size = params.validation_size,
            root_dir = config.root_dir,
            train_path = config.train_path,
            test_path = config.test_path,
            validation_path = config.validation_path,
            dataset_path = config.dataset_path
        )

        logger.info("data Spiltting configuration and params has been loaded successfully...")

        return splitting_dataset_config_params
    

    def get_preprocess_data_config_params(self) -> Preprocessing:
        """
        get the configuration and params for preprocessing the data
        Args:
            none
        Returns: 
            Preprocessing: return the structure of preprocessing config entity
        """
        config = self.config.preprocessing
        params = self.params.preprocessing

        preprocessing_config_params = Preprocessing(
            shuffle_size = params.shuffle_size,
            batch_size = params.batch_size,
            img_shape = params.img_shape
        )

        logger.info("preprocessing configuration and params has been loaded successfully...")

        return preprocessing_config_params
    

    def get_build_model_config_params(self) -> BUildModel:
        """
        get the configuration for building the model
        Args:
            None
        Returns:
            BuildModel: return the structure of the entity BuildModel
        """
        config = self.config.model_building
        params = self.params.model_building

        model_building_config_params = BUildModel(
            train_path = config.train_path,
            validation_path = config.validation_path,
            model_path = config.model_path
        )

        logger.info("Building model configuration and params has been loaded successfully..")

        return model_building_config_params