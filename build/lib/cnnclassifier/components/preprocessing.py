from cnnclassifier import logger
from cnnclassifier.entity.config_entity import Preprocessing
from cnnclassifier.config.configuration import configManager
import tensorflow as tf


# A class for preprocesing a data set
class preprocessing():
    def __init__(self, config_params: Preprocessing):
        """
        initialize all the params and configuration need for preprocessing the data
        Args:
            config_params(Preprocessing) : all the returns of the entity Preprocessing
        Returns:
            None
        """
        self.config_params = config_params #initialize the configuration and params
    
    def reshape_rescale(self,image,label):
        """
        reshape the images to (244,244,3) and rescale(normalize) to 1-0
        Args:
            image: the images we wll be reshaping and scaling
            label: the corresponding classification value of the image(0 or 1)
        Returns:
            A resized and rescale image with its corresponding classification value(0 or 1)
        """

        # perform rescale, reshape, add label
        return tf.image.resize(image,(self.config_params.img_shape,self.config_params.img_shape))/255.0, label

    def preprocess(self,dataset):
        """
        preprocess the data
        Args:
            dataset: the dataset we will be preprocessing
        Returns:
            None
        """
        try:
            logger.info("Data preprocessing has started...")
            # using the map function to preserve the classification value
            _dataset = dataset.map(self.reshape_rescale)

            # divide the dataset into batches, perform prefetching prefetch(autotune), and shuffle
            _dataset = _dataset.shuffle(self.config_params.shuffle_size).batch(self.config_params.batch_size).prefetch(tf.data.AUTOTUNE)
            logger.info("Data preprocessing has ended...")
        except Exception as e:
            raise e

        return _dataset
    
        # note the new shape th model will expert during testing or prediction is a batch shape so remember to batch that dataset(eg. u can do a batch of 1 : datast.batch(1))