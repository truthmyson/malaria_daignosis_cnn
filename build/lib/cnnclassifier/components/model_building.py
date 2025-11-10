from cnnclassifier import logger
from cnnclassifier.config.configuration import configManager
from cnnclassifier.entity.config_entity import BUildModel

import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense, InputLayer, Conv2D, MaxPooling2D, BatchNormalization, Flatten, Dropout
from keras.optimizers import Adam
from keras.losses import BinaryCrossentropy


# A class for building and training the model
class model_building:
    def __init__(self, config_params: BUildModel):
        """
        initialize the configuration and params
        Args:
            config_params(BuildModel): all the returns of the entity BuildModel
        Returns:
            None
        """
        self.config_params = config_params #initialize the configuration and params


    def build_model(self) -> Sequential:
        """
        define the structure and complie the model
        Args:
            None
        Returns:
            Sequential: return keras model sequential
        """
        try:
            logger.info("model building has started...")

            # model architecture
            model = Sequential([
                # define input layer
                InputLayer(shape=(244,244,3)),

                # FIRST BLOCK
                # 1st image convolution
                Conv2D(filters=9, kernel_size=(3,3),activation='relu'),
                # 2nd image convolution
                Conv2D(filters=18, kernel_size=(2,2), activation='relu'),
                # after the values might jump out of range, so normalize for 0 mean and 1 std
                BatchNormalization(),
                # 1st maxpooling
                MaxPooling2D(strides=(1,1)),

                # SECOND CONVOLUTION
                # 3nd image connvolution
                Conv2D(filters=32, kernel_size=(3,3), activation='relu'),
                # 4th image convolution
                Conv2D(filters=64, kernel_size=(2,2), activation='relu'),
                # after the values might jump out of range, so normalize for 0 mean and 1 std
                BatchNormalization(),
                # 2nd maxpooling
                MaxPooling2D(strides=(1,1)),

                # flatten the image for the NN
                Flatten(),

                # 1st NN
                Dense(units=512, activation='relu'),

                # 2nd NN
                Dense(units=128, activation='relu'),

                # 3rd NN
                Dense(units=32, activation='relu'),

                # 4th NN
                Dense(units=8, activation='relu'),

                # we will drop 30 percent to avoid over fitting
                Dropout(rate=0.3),

                # output layer
                Dense(units=1, activation='sigmoid')
            ])

            logger.info("model building has ended...")
        except Exception as e:
            raise e

        return model
    

    def compile_model(self, model: Sequential) -> Sequential:
        """
        compile the model for training
        Args:
            model(Sequential): model architcture that will be compiled
        Returns:
            Sequential: return keras model sequential
        """
        try:
            logger.info("modile compilation has started...")

            # compile model
            model.compile(
                optimizer=Adam(learning_rate=0.01),
                loss=BinaryCrossentropy(),
                metrics=['accuracy']
            )
            logger.info("modile compilation has ended...")
        except Exception as e:
            raise e

        return model
    

    def train_validate_model(self, model: Sequential, train_data, val_data):
        """
        train and validate the model
        Args:
            model(Sequential): the compile model we will be training
            train_data: the data for training the model
            val_data: the data for validating the model
        Returns:
            Sequential: return keras model sequential
            history: the models data for every epoch
        """
        try:
            logger.info("Model training has started...")

            # train the model with proper data formatting
            history = model.fit(
                train_data,
                validation_data=val_data,
                epochs=20,
                verbose=2
            )

            logger.info("Model training has ended...")
        except Exception as e:
            logger.error(f"Error during model training: {str(e)}")
            raise e
        
        return model, history
    
config = configManager()
m = model_building(config.get_build_model_config_params())
model = m.build_model()

model = m.compile_model(model)

from cnnclassifier.utils.common import read_dataset

train_data = read_dataset("artifacts/split_data/train")
val_data = read_dataset("artifacts/split_data/validate")

from cnnclassifier.components.preprocessing import preprocessing
p = preprocessing(config.get_preprocess_data_config_params())
train_data = p.preprocess(train_data)
val_data = p.preprocess(val_data)

model, history = m.train_validate_model(model, train_data, val_data)