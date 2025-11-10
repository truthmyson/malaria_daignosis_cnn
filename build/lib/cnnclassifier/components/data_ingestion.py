# we will download , split and save the data into a file
from cnnclassifier import logger
from cnnclassifier.config.configuration import configManager
from cnnclassifier.entity.config_entity import DataIngestionConfig
import tensorflow as tf
import tensorflow_datasets as tfds
import json
import os
from tensorflow.python.data.ops.load_op import _LoadDataset
from cnnclassifier.utils.common import read_dataset, read_text_file, save_dataset


# this is the data ingestion class
class data_ingestion():
    def __init__(self, config_params: DataIngestionConfig):
        """
        initialize all the params and configuration that will be need for the data ingestion
        Args:
            config_params(DataIngestionConfig) : this will hold all the returns of the entity DataIngestionConfig
        Returns:
            None
        """
        self.config_params = config_params #initialize the configuration and params

    def download_dataset(self):
        """
        download the malaria dataset and save it into a file(or dump it)
        Args:
            None
        Returns:
            None
        """
        if not os.path.exists(self.config_params.dataset_path) or not os.path.exists(self.config_params.dataset_info_path):
            try:
                logger.info("Downloading dataset has started...")

                # loading the dataset
                datasets, data_info = tfds.load(
                    self.config_params.dataset_name,
                    with_info = self.config_params.with_info,
                    shuffle_files = self.config_params.shuffle,
                    as_supervised = self.config_params.as_supervised,
                    split = self.config_params.split[0]
                )
                logger.info("downloading dataset has completed...")

                # saving the dataset with the corresponding labels
                save_dataset(datasets, self.config_params.dataset_path)

                # saving the info about the dataset
                with open(self.config_params.dataset_info_path, 'w') as f:
                    # Create a dictionary with relevant dataset info
                    info_dict = {
                        'name': data_info.name,
                        'description': data_info.description,
                        'version': str(data_info.version),
                        'features': str(data_info.features),
                        'splits': {k: int(v.num_examples) for k, v in data_info.splits.items()},
                        'citation': data_info.citation,
                        'homepage': data_info.homepage,
                    }
                    # Save as JSON for better structure and readability
                    json.dump(info_dict, f, indent=2)

                logger.info(f"dataset information has been saved successfully to: {self.config_params.dataset_info_path}")

            except Exception as e:
                raise e


    def ingest_dataset(self) -> _LoadDataset:
        """
        Ingest the dataset
        Args:
            None
        Returns:
            _LoadDataset: this is a tensorflow return type (actual - tensorflow.python.data.ops.load_op._LoadDataset)
        """
        # Load the dataset
        datasets = read_dataset(self.config_params.dataset_path)

        return datasets
    
    def get_dataset_info(self) -> list[str]:
        """
        Get information about the dataset
        Args:
            None
        Returns:
            str: returns a string
        """
        # load the information bout the dataset
        info = read_text_file(self.config_params.dataset_info_path)

        return info
