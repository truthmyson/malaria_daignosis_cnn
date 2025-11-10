from cnnclassifier import logger
from cnnclassifier.config.configuration import configManager
import tensorflow as tf
from cnnclassifier.entity.config_entity import SplitDatasets
from cnnclassifier.utils.common import read_dataset, save_dataset


# this is the m class for splitting the datasets
class split_dataset:
    def __init__(self, config_params: SplitDatasets):
        """
        Initialie all the params and configuration for splitting the dataset
        Args:
            config_params(SplitDatasets) : this will hold all the return of the entity SplitDatasets
        Returns:
            None
        """
        self.config_params = config_params # initialize all the params and configurations

    
    def split_train_test_val(self):
        """
        split and save the dataset into a training, testing, and validation datasets
        Args:
            NOne
        Returns:
            None
        """
        try:
            logger.info("Data splitting has begun...")

            # read or load the dataset
            dataset = read_dataset(str(self.config_params.dataset_path))

            len_dataset = len(dataset) # calculate the len of the dataset

            # the training dataset
            train_dataset = dataset.take(int(self.config_params.train_size * len_dataset))

            # gather the remaining dataset
            remaining_dataset = dataset.skip(int(self.config_params.train_size * len_dataset))
            len_remaining_dataset = len(remaining_dataset) # calculate the length of the remaining dataset

            # the testing dataset
            test_dataset = remaining_dataset.take(int(self.config_params.test_size * len_remaining_dataset))

            # gather the remiaing dataset
            remain_dataset = dataset.skip(int(self.config_params.test_size * len_remaining_dataset))
            len_remain_dataset = len(remain_dataset) # calculate the lenght of the remain dataset

            # validation dataset
            validate_dataset = remain_dataset.take(int(self.config_params.validation_size * len_remain_dataset))

            # save all dataset to a file
            save_dataset(train_dataset, self.config_params.train_path) #save the training dataset
            save_dataset(test_dataset, self.config_params.test_path) #save the testing dataset
            save_dataset(validate_dataset, self.config_params.validation_path) #save the validation dataset

            logger.info("Data splitting has ended...")
        except Exception as e:
            raise e