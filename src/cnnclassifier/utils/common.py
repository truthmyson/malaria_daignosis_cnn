# this will contain functions that will be needed  throughout the project
import os
from pathlib import Path
from typing import List
from cnnclassifier import logger
from ensure import ensure_annotations
from typeguard import typechecked
from box.exceptions import BoxValueError
from box import ConfigBox
import yaml
import tensorflow as tf
from tensorflow.python.data.ops.load_op import _LoadDataset
from tensorflow.python.data.ops.take_op import _TakeDataset



@typechecked #this function decorator will make sure all arguments follow strict type checking
def create_directory(path_to_create: List[str], verbose: bool=True) -> None:
    """
    create a directory(ies) if it doesn't exist
    Args:
        path_to_create (list[str]): paths or names of the directories to create
        verbose (bool, optional): whether to log info or not. Default = True
    Returns:
        None
    """
    try:
        for path in path_to_create:
            os.makedirs(path, exist_ok=True)

            if verbose:
                logger.info(f"created directory: {path}")
    except Exception as e:
        raise e


@typechecked #this function decorator will make sure all arguments follow strict type checking
def create_file(file_path: List[str], verbose: bool=True) -> None:
    """
    create a file(s) if it doesn't exist
    Args:
        file_path (list[str]): paths or names of the files to create
        verbose (bool, optional): whether to log info or not. Default = True
    Returns:
        None
    """
    try:
        for file in file_path:
            _path = Path(file) #get the root path
            folder, path = os.path.split(_path) #check if file path included
            if not path=="":
                _path.touch(exist_ok=True) #create file path if it exist
                if verbose:
                    logger.info(f"created file: {file}")
            else:
                raise ValueError(f"file path not provided: {file}")
    except Exception as e:
        raise e
    

@ensure_annotations #this function decorator will make sure all arguments follow strict type checking
def read_yaml(file_path: Path) -> ConfigBox:
    """
    Read the content of a yaml file
    Args:
        file_path (Path): path to the yaml file
        verbose (bool, optional): whether to log info or not. Default = True
    Returns:
        Configbox: returns the content of the yaml file as configbox(that is it can be accessed like a 'dict_name[key]' or 'dict_name.key')
    """
    ends_with = str(file_path).endswith('.yaml')

    if ends_with:
        try:
            with open(file_path, 'r') as yaml_file:
                content = yaml.safe_load(yaml_file)
                return ConfigBox(content)
        except BoxValueError as e: #boxvalueerror is raised when the return time type is none or empty str
            raise ValueError(f"yaml file is empty: {e}")
        except Exception as e:
            raise e
    else:
        raise ValueError(f"the provided file is not a yaml file: {file_path}")
    
@typechecked
def read_dataset(dataset_path: str, verbose: bool=True) -> _LoadDataset:
    """
    load the dataset from the path provided.
    Args:
        dataset_path(Path): the path to the dataset
        verbose (bool, optional): whether to log info or not. Default = True
    Returns:
        _LoadDataset: this is a tensorflow dataset type(actual - tensorflow.python.data.ops.load_op._LoadDataset) 
    """
    try:
        dataset_path = str(Path(dataset_path))
        # load the datasets
        datasets = tf.data.Dataset.load(dataset_path)
        if verbose:
            logger.info("Datasets has been loaded successfullly...")

        return datasets
    except Exception as e:
        raise e
    

@typechecked
def read_text_file(file_path: Path|str, verbose: bool=True) -> list[str]:
    """
    load a text file
    Args:
        file_path(Path): the path to the text file
        verbose (bool, optional): whether to log info or not. Default = True
    Returns:
        str: return a formatted string object
    """
    try:
        # convert file path if is string, to Path object
        if isinstance(file_path, str):
            file_path = Path(file_path)

        with open(file_path, 'r') as f:
            data = f.read() #read the content of file as string

            # format the string
            data = data.replace('\n',"").replace("\\n"," ").replace("\'","").replace("  "," ").replace('"',"")
            data = data.split('",')


            if verbose:
                logger.info(f"file has been read successfully {file_path}")
            return data
    except Exception as e:
        raise e
    
@typechecked
def save_dataset(dataset: _TakeDataset, dataset_path: str, verbose: bool=True):
    """
    save the dataset to the path provided.
    Args:
        dataset(_LoadDataset): the dataset we want to save
        dataset_path(Path): the path to the dataset
        verbose (bool, optional): whether to log info or not. Default = True
    Returns:
        None
    """
    try:
        if not os.path.exists(dataset_path):
            # save the dataaset
            tf.data.Dataset.save(dataset, dataset_path)
            if verbose:
                logger.info(f"Dataset has been saved successfully to: {dataset_path}")

    except Exception as e:
        raise e